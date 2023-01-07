from django.shortcuts import redirect
from .forms import UserForm
from django.contrib import messages
import logging
from .models import User
from django.shortcuts import render
from django_tables2 import RequestConfig
from django_tables2 import SingleTableView
from .tables import UserTable


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
                return redirect('register')
            except Exception as e:
                print(e)
                raise e

    else:
        userform = UserForm()
    return render(request, 'user/register.html', {'user': userform})


def home(request):
    table = UserTable(User.objects.all())
    model = User
    table_class = UserTable
    RequestConfig(request).configure(table)
    return render(request, 'user/home.html', {'table': table})


class UserListView(SingleTableView):
    model = User
    table_class = UserTable
    template_name = 'user/user.html'