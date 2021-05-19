from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Todo

# Create your views here.
def homepage(request):
    todos = Todo.objects.all()
    return render(request, 'main/home.html', {'todos': todos})

@login_required
def user_detail(request):
    todos = Todo.objects.filter(user=request.user, done=False)
    return render(request, 'main/mytodos.html', {'todos': todos})
