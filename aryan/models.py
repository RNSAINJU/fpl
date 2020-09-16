from django.db import models
from django.conf import settings
import os
import random

def get_filename_ext(filepath):
    base_name=os.path.basename(filepath)
    name,ext=os.path.splitext(base_name)
    return name,ext

def user_image_path(instance, filename):
    new_filename=random.randint(1,1234567890)
    name,ext=get_filename_ext(filename)
    final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "company/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )

def winner_image_path(instance, filename):
    new_filename=random.randint(1,123456789)
    name, ext=get_filename_ext(filename)
    final_filename='{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return "winner/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )

class Teams(models.Model):
    ACTIVE_CHOICES=(
        ('yes','Yes'),
        ('no','No'),
    )
    # user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    name=models.CharField(max_length=30, unique=True)
    teamname=models.CharField(max_length=30, unique=True)
    active=models.CharField(max_length=10,choices=ACTIVE_CHOICES,default='no')
    date=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.name

class Company(models.Model):
    STATUS_CHOICES=(
    ('active','Active'),
    ('in-active','In-active'),
    )
    name=models.CharField(max_length=30,unique=True)
    address=models.CharField(max_length=40)
    phone_no=models.IntegerField(null=True)
    short_description=models.CharField(max_length=80, unique=True)
    description=models.TextField(unique=True)
    description2=models.TextField(unique=True,blank=True)
    name_in_style= models.CharField(max_length=30, unique=True)
    logo=models.ImageField(upload_to=user_image_path, null=True, blank=False)
    image1=models.ImageField(upload_to=user_image_path, null=True, blank=True)
    image2=models.ImageField(upload_to=user_image_path, null=True, blank=True)
    fb_link=models.CharField(max_length=100, unique=True)
    teams=models.ManyToManyField(Teams)
    # winner=models.OneToOneField(Winner, on_delete=models.CASCADE)
    rewards=models.ImageField(upload_to=user_image_path, null=True, blank=True)
    # collection=models.ManyToManyField(Teams)



class Gameweekwinner(models.Model):
    name=models.OneToOneField(Teams,on_delete=models.CASCADE)
    no=models.IntegerField(unique=True,blank=False)
    points=models.IntegerField(unique=True,blank=False)

    def __str__(self):
        return self.name.name

class Winner(models.Model):
    name=models.OneToOneField(Teams,on_delete=models.CASCADE)
    Year=models.IntegerField(unique=True,blank=False)
    image=models.ImageField(upload_to=winner_image_path,null=True,blank=False)
    points=models.IntegerField(unique=True,blank=False)
    voice=models.TextField(unique=True,blank=False)

    def __str__(self):
        return self.name.name

# class Collection(models.Model):
#     FEATURED_CHOICES=(
#         ('yes','Yes'),
#         ('no','No'),
#     )
#     # user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     name=models.CharField(max_length=30, unique=True)
#     short_description=models.CharField(max_length=80, unique=True)
#     image=models.ImageField(upload_to=users_image_path,null=True,blank=False)
#     featured=models.CharField(max_length=10,choices=FEATURED_CHOICES,default='no')
#     date=models.DateTimeField(auto_now_add=True,blank=True)

#     def __str__(self):
#         return self.name