import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasgowRPG.settings')
django.setup()
from django.contrib.auth.models import User
from rpg.models import UserProfile


def populate():

    #Three test users and their profiles
    add_user(username="Chris1",email="2030808m@student.gla.ac.uk",password="test")
    add_userprofile(picture = None,user_id=1, displayname = "christopher", academic_score = 55,
    social_score = 52, no_grads = 1, no_viper = 0, no_homework = 8, no_tennent = 10, no_drop = 2)

    add_user(username="Han2",email="2288527@student.gla.ac.uk",password="test")
    add_userprofile(picture = None,user_id=2, displayname = "Nicholas", academic_score = 40,
    social_score = 60, no_grads = 2, no_viper = 6, no_homework = 5, no_tennent = 12, no_drop = 1)

    add_user(username="Euan3",email="2261718@student.gla.ac.uk",password="test")
    add_userprofile(picture = None,user_id=3, displayname = "Temp", academic_score = 30,
    social_score = 70, no_grads = 5, no_viper = 15, no_homework = 3, no_tennent = 11, no_drop = 4)





def add_user(username,email,password):
    user = User.objects.create_user(username=username,
                                 email=email,
                                 password=password)
    return user

def add_userprofile(picture, user_id,displayname,academic_score,social_score,no_grads,no_viper,no_homework,no_tennent,no_drop):


    userprof = UserProfile(picture, user_id ,displayname,academic_score,social_score,no_grads,no_viper,no_homework,no_tennent,no_drop)
    userprof.save()

    return userprof



if __name__ == '__main__':
    print ("Starting rpg population script...")

    populate()