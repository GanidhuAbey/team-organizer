from django.db import models
# Create your models here.

class TeamMember(models.Model):
    first_name = models.TextField(max_length=200)
    last_name = models.TextField(max_length=200)

    #not sure if we need to keep track of the internation code?
    phone_number = models.IntegerField(default="0")
    email = models.EmailField(max_length = 254, default="test@example.com")

    profile_picture = models.CharField(default='profile_icon.jpg', max_length=200)

    class Role(models.IntegerChoices):
        REGULAR = 0;
        ADMIN = 1;

    role = models.IntegerField(Role.choices, default=0)

