from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.forms import ModelForm
from .models import Post, Business, Profile

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.pop("autofocus", None)

class NewPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'post', 'type']

class NewBusinessForm(ModelForm):
    class Meta:
        model = Business
        exclude = ['user', 'neighborhood']

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class ChangeNeighborhoodForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['neighborhood']