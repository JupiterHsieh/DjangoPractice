from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models
import uuid

# Create your models here.
# 在這裡 Project 和 Review 是一對多關係  Project 和Tag是多對多關係



class Project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(null=True,blank=True) #can be empty
    featured_image = models.ImageField(null=True,blank=True,default="default.jpg")
    demo_link = models.CharField(max_length = 2000, null=True, blank=True)
    source_link = models.CharField(max_length = 2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True) #與下面的Tag 是 Many to Many 關係 #重要
    vote_total = models.IntegerField(default=0,null=True, blank=True)
    vote_ratio = models.IntegerField(default=0,null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)

    
    def __str__(self):
        return self.title



class Review(models.Model):
    VOTE_TYPE = (
        ('up','UP Vote'),
        ('down','Down Vote'),
    )
    #owner
    project = models.ForeignKey(Project, on_delete=models.CASCADE) #重要
    body = models.TextField(null=True,blank=True)
    value =  models.CharField(max_length = 200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)

    def __str__(self):
        return self.value

# create a many to many relation between upper two

class Tag(models.Model):
    name = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)

    def __str__(self):
        return self.name




    




 