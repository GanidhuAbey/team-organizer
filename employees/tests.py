from django.test import TestCase
from django.test.client import RequestFactory
from django.test import Client
from django.urls import reverse
from random import randint


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


    def test_team_list(self):
        response = self.client.get(reverse("display"))
        self.assertEqual(response.status_code, 200) 

    def test_handle_add_request(self):
        request = self.factory.get(reverse("add"))
 
        response = views.add_page(request);

        self.assertEqual(response.status_code, 200)

    def test_handle_edit_request(self): 
        c = Client()
        response = c.get(reverse("edit"), data={"member_index": "1"})

        self.assertEqual(response.status_code, 200)

    #test if correct member is being edited with get request
    def test_edit_member_request(self):
        c = Client()
        member = models.TeamMember.objects.get(pk=self.member_indices[0])

        response = c.get(reverse("edit"), data={"member_index": member.member_index})

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

 
    def test_add_member_post(self):
        c = Client()

        teamCount = len(self.member_indices)
        data = {"first_name": "test", "last_name": "1", "phone_number": "1234667890", "email": "test@gmail.com", "role": 0, "member_index": str(teamCount+1)}

        c.post(reverse("add"), data=data)
 
        otherwise = True
        newTeamCount = models.TeamMember.objects.all().count()
        if newTeamCount > teamCount:
            new_member = models.TeamMember.objects.get(pk=teamCount+1)
            if (new_member.phone_number == "1234667890"):
                self.assertTrue(True);
                otherwise = False
                
        if otherwise:
            self.assertTrue(False)

    def test_edit_member_post(self):
        c = Client()

        random_id = randint(1, len(self.member_indices))
        member = models.TeamMember.objects.get(pk=random_id)
 
        first_name = member.first_name
        email = member.email
        phone_number = member.phone_number
        role = member.role

        data = {"first_name": first_name, "last_name": "NEWNAME", "phone_number": phone_number, "email": email, "role": role, "member_index": random_id}

        c.post(reverse("edit"), data=data)

        updated_member = models.TeamMember.objects.get(pk=random_id)

        if updated_member.last_name == "NEWNAME":
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_edit_valid_input(self):
        c = Client()

        random_id = randint(1, len(self.member_indices))
        member = models.TeamMember.objects.get(pk=random_id)
 
        first_name = member.first_name
        last_name = member.last_name
        phone_number = member.phone_number
        email = member.email
        role = member.role

        invalid_phone_numbers = ["4103101619", "410-310-1619", "410 310 1619", "+1 410 310 1619", "+1-410-310-1619"]
        invalid_emails = ["email@domain.com", "email@domain.net", "email.som@domain.net"]

        def push_bad_input_to_server(data): 
            response = c.post(reverse("edit"), data=data)
            self.assertEqual(response.status_code, 302) 

        for bad_pnum in invalid_phone_numbers:
            data = {"first_name": first_name, "last_name": last_name, "phone_number": bad_pnum, "email": email, "role": role, "member_index": random_id}
            push_bad_input_to_server(data)

        for bad_email in invalid_emails:
            data = {"first_name": first_name, "last_name": last_name, "phone_number": phone_number, "email": bad_email, "role": role, "member_index": random_id}
            push_bad_input_to_server(data)


    def test_edit_invalid_input(self):
        c = Client()

        random_id = randint(1, len(self.member_indices))
        member = models.TeamMember.objects.get(pk=random_id)
 
        first_name = member.first_name
        last_name = member.last_name
        phone_number = member.phone_number
        email = member.email
        role = member.role

        invalid_phone_numbers = ["text input", "123", "123 312 1413 1", "++413-430-1023"]
        invalid_emails = ["email_no_domain", "email.com", "email@.com"]

        def push_bad_input_to_server(data): 
            response = c.post(reverse("edit"), data=data)
            self.assertEqual(response.status_code, 400) 

        for bad_pnum in invalid_phone_numbers:
            data = {"first_name": first_name, "last_name": last_name, "phone_number": bad_pnum, "email": email, "role": role, "member_index": random_id}
            push_bad_input_to_server(data)

        for bad_email in invalid_emails:
            data = {"first_name": first_name, "last_name": last_name, "phone_number": phone_number, "email": bad_email, "role": role, "member_index": random_id}
            push_bad_input_to_server(data)






