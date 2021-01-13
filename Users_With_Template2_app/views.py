from django.shortcuts import render, redirect
from .models import Users


# Create your views here.
def index(request):
    print("------------we are in the index------------")
    all_user = Users.objects.all()
    print('********', type(all_user))

    context = {
        "new_user": all_user
    }

    return render(request, 'index.html', context)
    


def add_user(request):
    Users.objects.create(first_name=request.POST['user_first_name'],
    last_name=request.POST['user_last_name'], 
    email_address=request.POST['user_email'], 
    age=request.POST['user_age'])
    return redirect('/')
