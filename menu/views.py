# views.py in menu app

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Food
from profiles.models import Comment
from django.http import JsonResponse

def food_list(request):
    foods = Food.objects.all()
    foods_by_category = {}
    for category, _ in Food.CATEGORIES:
        foods_by_category[category] = foods.filter(category = category)
    return render(request , 'menu/list.html' , {'foods_by_category' : foods_by_category})

def food_detail(request, slug):
    food_detail = get_object_or_404(Food, slug = slug)
    comments = food_detail.comments.filter(active = True)
    new_comment = None

    if request.method == 'POST':
        name = request.POST.get('commenter_name')
        email = request.POST.get('commenter_email')
        body = request.POST.get('comment_text')

        if name and body:
            new_comment = Comment(
                food = food_detail,
                name = name,
                email = email,
                body = body,
                active = False
            )
            new_comment.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True})
            messages.success(request, 'Your comment has been submitted for review.')
            return redirect('menu:detail', slug=food_detail.slug)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'error': 'Please fill out all fields.'})
            messages.error(request, 'Please fill out all required fields.')

    context = {
        'food_detail': food_detail,
        'comments': comments,
        'new_comment': new_comment,
    }

    return render(request , 'menu/detail.html' , context)