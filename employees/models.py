from django.db import models
from django.forms import ModelForm
from django.core.validators import RegexValidator
# Create your models here.

class TeamMember(models.Model):
    member_index = models.BigAutoField(primary_key=True)

    first_name = models.TextField(max_length=200)
    last_name = models.TextField(max_length=200)

    #not sure if we need to keep track of the internation code?
    phone_regex = RegexValidator(regex=r'([+][0-9])?[-| ]?[0-9]{3}[-| ]?[0-9]{3}[-| ]?[0-9]{4}$', message="Invalid phone number")
    phone_number = models.CharField(validators=[phone_regex], default="0", max_length=17)
    email = models.EmailField(max_length = 254, default="test@example.com")

    profile_picture = models.CharField(default='profile_icon.jpg', max_length=200)

    class Role(models.IntegerChoices):
        REGULAR = 0;
        ADMIN = 1;

    role = models.IntegerField(Role.choices, default=0)


class TeamMemberForm(ModelForm):
    class Meta:
        model = TeamMember
        fields = ['member_index', 'first_name', 'last_name', 'phone_number', 'email', 'role'] #add role, profile icon not in scope of project
