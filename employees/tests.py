from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse

from . import models
from . import views

# Create your tests here.
class MemberListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        #create team members
        teamCount = 10
        
        cls.member_indices = []

        for member_id in range(teamCount):
            member = models.TeamMember(first_name="firstName", last_name=str(member_id), phone_number="1234567890", email="example@domain.com")
            member.save()
            cls.member_indices.append(member.member_index)

        cls.factory = RequestFactory()


    def test_view_team_list(self):
        response = self.client.get(reverse("display"))
        self.assertEqual(response.status_code, 200) 

    def test_view_handle_add_request(self):
        request = self.factory.get(reverse("add"))
 
        response = views.add_page(request);

        self.assertEqual(response.status_code, 200)

    def test_view_handle_edit_request(self): 
        request = self.factory.get(reverse("edit"), data={"member_index": "1"})

        response = views.edit_page(request);

        self.assertEqual(response.status_code, 200)

    #test if correct member is being edited with get request
    def test_view_edit_member_request(self):
        member = models.TeamMember.objects.get(pk=self.member_indices[0])

        request = self.factory.get(reverse("edit"), data={"member_index": member.member_index})

        response = views.edit_page(request);

        self.assertEqual(response.status_code, 200)

        #check that member data is produced in html
        first_name = member.first_name
        last_name = member.last_name
        email = member.email
        phone_number = member.phone_number
        role = member.role

        self.assertContains(response, text=first_name)
        self.assertContains(response, text=last_name)
        self.assertContains(response, text=email)
        self.assertContains(response, text=phone_number)
        self.assertContains(response, text=role)

 
    def test_view_add_member_post(self):
        teamCount = len(self.member_indices)
        data = {"first_name": "test", "last_name": "1", "phone_number": "1234667890", "email": "test@gmail.com", "role": 0, "member_index": str(teamCount+1)}

        request = self.factory.post(reverse("add"), data=data)

        views.add_page(request)
        
        otherwise = True
        newTeamCount = models.TeamMember.objects.all().count()
        if (newTeamCount > teamCount):
            new_member = models.TeamMember.objects.get(pk=teamCount+1)
            if (new_member.phone_number == 1234667890):
                self.assertTrue(True);
                otherwise = False
                
        if (otherwise):
            self.assertTrue(False)

    def test_view_edit_member_post(self):
        member = models.TeamMember.objects.get(pk=self.member_indices[0])
 
        first_name = member.first_name
        email = member.email
        phone_number = member.phone_number
        role = member.role

        data = {"first_name": first_name, "last_name": "NEWNAME", "phone_number": phone_number, "email": email, "role": role, "member_index": self.member_indices[0]}

        request = self.factory.post(reverse("edit"), data=data)

        views.edit_page(request);

        updated_member = models.TeamMember.objects.get(pk=self.member_indices[0])

        if (updated_member.last_name == "NEWNAME"):
            self.assertTrue(True)
        else:
            self.assertFalse(True)






