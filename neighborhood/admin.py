from django.contrib import admin

from .models import Profile, Gender, Post, Neighborhood, Business

admin.site.register(Profile)
admin.site.register(Gender)
admin.site.register(Post)
admin.site.register(Neighborhood)
admin.site.register(Business)
