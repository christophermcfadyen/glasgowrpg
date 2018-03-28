import os

def populate():
    add_user(username="Chris",email="2030808m@student.gla.ac.uk",password="test")
    add_userprofile(picture = None, displayname = "Chris203", academic_score = 50,
    social_score = 50, no_grads = 3, no_viper = 2, no_homework = 1, no_tennent = 12, no_drop = 1)



def add_user(username,email,password):
    u = User.objects.get_or_create(username=username,email=email,password=password)[0]
    return u

def add_userprofile(picture, displayname,academic_score,social_score,no_grads,no_viper,no_homework,no_tennent,no_drop):
    userprof = UserProfile.get_or_create(picture, displayname,
    academic_score,social_score,no_grads,no_viper,no_homework,no_tennent,no_drop)[0]

    return userprof



if __name__ == '__main__':
    print ("Starting rpg population script...")
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'glasgowRPG.settings')
    from rpg.models import User, UserProfile
    populate()