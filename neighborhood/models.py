from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver

from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField


class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.TextField()
    manager_name = models.CharField(max_length=100, blank=True)
    manager_number = models.CharField(max_length=20, blank=True)
    manager_email = models.EmailField(blank=True)
    hospital_name = models.CharField(max_length=100, blank=True)
    hospital_number = models.CharField(max_length=20, blank=True)
    hospital_email = models.EmailField(blank=True)
    police_name = models.CharField(max_length=100, blank=True)
    police_number = models.CharField(max_length=20, blank=True)
    police_email = models.EmailField(blank=True)
    hood_pic = CloudinaryField('images', default='image/upload/v1627343010/neighborhood1_cj2fyx.jpg')

    @property
    def occupants_count(self):
        return Profile.objects.filter(neighborhood=self).count()

    def __str__(self):
        return self.name
    
    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, neighborhood_id):
        return cls.objects.filter(id=neighborhood_id)

    @classmethod
    def update_neighborhood(cls,id,name):
        return cls.objects.filter(id=id).update(name=name)

class Gender(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
        
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile') 
    house = models.CharField(max_length=50)
    phase = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    profile_picture = CloudinaryField('image', default='image/upload/v1626430054/default_zogkvr.png')

    neighborhood = models.ForeignKey(Neighborhood,on_delete=models.SET_NULL, null=True,related_name='neighbors',blank=True)

    def __str__(self):
        return f'{self.user.username} profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, search_term):
        return cls.objects.filter(user__username__icontains=search_term).all()
    def __str__(self):
        return f'{self.user.username} Profile'

class Business(models.Model):
    name=models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    start_day = models.CharField(max_length=50)
    end_day = models.CharField(max_length=50)
    open_time = models.TimeField()
    close_time = models.TimeField()
    bs_image = CloudinaryField('images', default='image/upload/v1627341811/company_default_qb4ili.png')

    user=models.ForeignKey(Profile, on_delete=models.CASCADE) 
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, business_id):
        return cls.objects.filter(id=business_id)

    @classmethod
    def update_business(cls,id,name):
        update = cls.objects.filter(id=id).update(name=name)
        return update

class PostType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=120, null=True)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    type = models.ForeignKey(PostType, on_delete=models.CASCADE, related_name='posts')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    hood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title

    @classmethod
    def search_post(cls, search_term):
        return cls.objects.filter(title__icontains=search_term).all()