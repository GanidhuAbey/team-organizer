from django.shortcuts import render
from django.shortcuts import redirect
from json import dumps
#import model data
from . import models

#TODO: generalize display_page, add_page, and edit_page in a class-based generic
# Create your views here.
def display_page(request):
    #check how many team members we have
    all_team_members = models.TeamMember.objects.all()
    team_count = all_team_members.count()

    obj_list = list(models.TeamMember.objects.values())
    json_string = dumps([ob for ob in obj_list])

    return render(request, 'display.html', context={"teamCount" : str(team_count), "dataTeam" : json_string})

def add_page(request):
    return render(request, 'add.html')

def edit_page(request):
    #need to attach some extra data to this request
    member_index = request.GET.get('member_index');
    member = models.TeamMember.objects.get(id=member_index);
    first_name = member.first_name;
    last_name = member.last_name;
    email = member.email;
    return render(request, 'edit.html', context={"fname" : first_name, "lname" : last_name, "email" : email, "member_index" : str(member_index)})

def edit_team_member(request):
    member = models.TeamMember.objects.get(id=request.POST['member_index'])
    if 'delete_button' in request.POST:
        #delete object from database
        member.delete() 
        return redirect('/employees/display/')
   
    #else safely assume that user meant to update team member 
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    email = request.POST['email']

    member.first_name = first_name
    member.last_name = last_name
    member.email = email

    member.save()

    return redirect('/employees/display/')


def add_team_member(request):
    #every time update team count is called we need to add a team member
    first_name = request.POST['fname']
    last_name = request.POST['lname']
    email = request.POST['email']
    new_member = models.TeamMember(first_name=first_name, last_name=last_name, email=email);
    new_member.save()
    return redirect('/employees/display/')

