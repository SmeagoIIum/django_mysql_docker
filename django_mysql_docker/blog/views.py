from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from user.models import User

# Create your views here.


def home(request):
    context = {'users': User.objects.all}
    return render(request, 'blog/home.html', context)


# def about(request):
#     return render(request, 'blog/about.html', {'title': 'About'})


