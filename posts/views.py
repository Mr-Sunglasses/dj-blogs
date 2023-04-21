from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from posts.forms import PostForm, UserRegisterForm
from posts.models import Post
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
@login_required()
def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f"Post Created Successfully")
            return redirect("/welcome")
    else:
        form = PostForm()
    context = {
        "form": form
    }
    return render(request, "posts/new_post.html", context=context)


def details(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {
        "post": post
    }
    return render(request, "posts/details.html", context=context)

@login_required()
def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    messages.warning(request, "Post Deleted")
    return redirect("/welcome")


def sign_up(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            new_user = authenticate(
                username= username,
                password=form.cleaned_data["password1"]
            )
            login(request, new_user)
            messages.success(request, f'Account Created For {username}')
            return redirect("/welcome")
    else:
        form = UserRegisterForm()
    context = {
        "form": form
    }
    return render(request, "registration/register.html", context=context)
