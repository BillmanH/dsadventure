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
        context = {}
        context['formData']  = yaml.load(request.POST.get("formData","No data found"),yaml.SafeLoader)
        world = the_first_age(context['formData'])
        #individual items are cast into lists (easier than parsing a dataframe.to_dict() in json
        context['df_features'] = world.df_features.T.to_dict()
        context['keys'] = world.df_features['key'].to_list()
        context['elevation'] = world.df_features['elevation'].to_list()
        context['rainfall'] = world.df_features['rainfall'].to_list()
        context['terrain'] = world.df_features['terrain'].to_list()

        return render(request,'game/show_world01.html',context)
    else:
        return render(request, 'game/show_world01.html')


