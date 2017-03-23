from django.shortcuts import render
from django.utils import timezone
from .models import Club

def post_list(request):
    posts = Club.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'model/post_list.html', {'posts': posts})