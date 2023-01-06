from django.shortcuts import render, redirect
from .forms import UserForm, User
from django.contrib import messages
import logging


def register(request):
    logging.warning('REGISTER function is triggered')
    if request.method == "POST":
        userform = UserForm(request.POST)
        logging.warning('UserForm with POST request is triggered')
        for field in userform:
            logging.warning("Field Error:" + field.name + field.errors)
        if userform.is_valid():
            logging.warning('UserForm is valid')
            try:
                userform.save()
                name = userform.cleaned_data.get('first_name')
                messages.success(request, f'User created: {name}')
                return redirect('blog-home')
            except Exception as e:
                print(e)
                raise e

    else:
        userform = UserForm()
    return render(request, 'user/register.html', {'user': userform})
