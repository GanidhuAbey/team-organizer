from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import ListView
from django.urls import reverse
import phonenumbers


#import model data
from . import models

#TODO: generalize display_page, add_page, and edit_page in a class-based generic
# Create your views here.

class MemberList(ListView):
    model = models.TeamMember
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team_count = models.TeamMember.objects.all().count()
        context['teamCount'] = team_count
        return context


def add_page(request):
    if request.POST:
        member_form = models.TeamMemberForm(request.POST) 
        if member_form.is_valid():
            member_form.save()
        else:
            print(member_form.errors)
            return render(request, "add.html", context={"formData" : member_form.errors.as_json()}, status=400)

        return redirect("display")

    return render(request, 'add.html')

def edit_page(request):
    if request.POST:
        member = models.TeamMember.objects.get(pk=int(request.POST['member_index']))
        if 'delete_button' in request.POST:
            #delete object from database
            member.delete() 
            return redirect(reverse("display"))
       
        #else safely assume that user meant to update team member 
        update_member = models.TeamMemberForm(request.POST, instance=member)
        if update_member.is_valid(): 
            update_member.save()
        else:
            first_name = member.first_name;
            last_name = member.last_name;
            phone_number = member.phone_number;
            email = member.email;
            role = str(member.role);
            if (role == "0"):
                role = ""
            member_index = request.POST['member_index']
            return render(request, 'edit.html', context={"fname" : first_name, "lname" : last_name, "email" : email, "pnum" : phone_number, "role" : role, "member_index" : member_index, "formData": update_member.errors.as_json()}) 

        return redirect(reverse("display"))


    member_index = request.GET.get('member_index'); 
    member = models.TeamMember.objects.get(pk=int(member_index));
    first_name = member.first_name;
    last_name = member.last_name;
    phone_number = member.phone_number;
    email = member.email;
    role = str(member.role);
    if (role == "0"):
        role = ""
    return render(request, 'edit.html', context={"fname" : first_name, "lname" : last_name, "email" : email, "pnum" : phone_number, "member_index" : member_index, "role" : role}) 

