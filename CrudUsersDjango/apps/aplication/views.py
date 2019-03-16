from django.shortcuts import render
from .models import *
from .forms import userform
# Create your views here.

def home(req):
    return render(req,'index.html')

def crearUser(req):
    if req.method == 'POST':
        form = userform(req.POST)
        if form.is_valid():
            form.save()
            return render(req,'index.html')
        else:
            form = userform()
        return render(req, 'aplication/users.html', {'form':form})
    else:
        form = userform()
        return render(req, 'aplication/users.html', {'form':form})