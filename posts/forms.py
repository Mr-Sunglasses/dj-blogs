from django.forms import ModelForm, Textarea, TextInput, EmailField
from posts.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ('author','time')
        widgets = {
            'title': TextInput(),
            'body': Textarea(),
        }


class UserRegisterForm(UserCreationForm):
    email = EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
