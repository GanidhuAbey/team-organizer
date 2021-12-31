from django.shortcuts import render
from django.shortcuts import redirect
from django.http import JsonResponse
from json import dumps
#import model data
from . import models

#TODO: can probably converge index and add page into one function using class generics

# Create your views here.
def index(request):
    #check how many team members we have
    all_team_members = models.TeamMember.objects.all()
    team_count = all_team_members.count()

    obj_list = list(models.TeamMember.objects.values())
    json_string = dumps([ob for ob in obj_list])

    return render(request, 'display.html', context={"teamCount" : str(team_count), "dataTeam" : json_string})


def add_team_member(request):
    #every time update team count is called we need to add a team member
    first_name = request.GET.get('fname')
    last_name = request.GET.get('lname')
    email = request.GET.get('email')
    new_member = models.TeamMember(first_name=first_name, last_name=last_name, email=email);
    new_member.save()
    return redirect('/employees/display/')

#render add member form
def add_page(request):
    return render(request, 'add.html')
