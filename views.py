from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def start_screen(request):
    return render(request,'game/start_screen.html')

@login_required
def create_world_01(request):
    context = {"foo":"bar"}
    if "GET" == request.method:
        return render(request,'game/create_world01.html')
    else: 
        return render(request, 'game/create_world01.html')

@login_required
def show_world_01(request):
    if "POST" == request.method:
        return render(request,'game/show_world01.html')
    else:
        return render(request, 'game/show_world01.html')

