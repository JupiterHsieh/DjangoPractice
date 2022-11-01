#@receiver(post_save, sender=Profile)
from django.contrib.auth.models import User 
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile

def createProfile(sender, instance, created, **kwargs):
    print('Profile signal trigger')
    if created:
        user = instance #instance 跟sender 是一樣的 
        #創新user的時候同時創user 的profile 
        profile = Profile.objects.create(
            user = user,
            username=user.username,
            email=user.email,
            name=user.first_name,


        )
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()
    print("Deleting user... ")
    print("Instance: ", instance)
     

post_save.connect(createProfile,sender=User) #sender == time to trigger this signal
post_delete.connect(deleteUser, sender=Profile)