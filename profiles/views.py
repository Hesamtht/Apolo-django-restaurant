from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from menu.models import Food
from .models import Comment

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            messages.error(request, 'Password and Confirm Password do not match')
            return redirect('profiles:register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'This email is already registered')
            return redirect('profiles:register')

        user = User.objects.create_user(username = email , email = email , password = password)
        user.first_name = name
        user.save()
        messages.success(request , 'Registration successful')

        user = authenticate(request , username = email , password = password)
        if user is not None:
            login(request , user)
            return redirect('home:home')

    return render(request , 'register_form.html')

def comment(request , slug):
    food_detail = get_object_or_404(Food , slug = slug)
    comments = Comment.objects.filter(food = food_detail , active = True)
    new_comment = None

    if request.method == 'POST':
        name = request.POST.get('commenter_name')
        body = request.POST.get('comment_text')
        if name and body:
            new_comment = Comment.objects.create(
                food = food_detail,
                name = name,
                body = body,
                active = False
            )
            messages.success(request , 'Your comment has been submitted for review.')
            return redirect('menu:detail' , slug = food_detail.slug)

    context = {
        'food_detail': food_detail,
        'comments': comments,
        'new_comment': new_comment,
    }

    return render(request , 'menu/templates/detail.html' , context)
