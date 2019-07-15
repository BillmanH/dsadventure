from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .lib.create_world import *
import yaml

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
        context = {"formData":""}
        context['formData']  = yaml.load(request.POST.get("formData","No data found"),yaml.SafeLoader)
        world = the_first_age(context['formData'])
        context['df_features'] = world.df_features.T.to_dict()
        context['grid_elevation'] = world.grid_elevation.T.to_dict()
        context['grid_rainfall'] = world.grid_rainfall.T.to_dict()
        return render(request,'game/show_world01.html',context)
    else:
        return render(request, 'game/show_world01.html')


