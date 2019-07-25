from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .lib.create_world import *
from .lib.boto import s3Transfer as b
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
        #post the `world` to an s3 bucket, using the username as the key
        user = request.user.get_username()
        b.save_world(world,user)
        #building a dictionairy in the format that d3.js will prefer
        wa = [world.df_features.loc[m].to_dict() for m in world.df_features.index]
        context['df_features'] = wa
        context['dim_1'] = np.unique(world.df_features['x']).tolist() 
        context['dim_2'] = np.unique(world.df_features['y']).tolist()
        return render(request,'game/show_world01.html',context)
    else:
        return render(request, 'game/show_world01.html')

@login_required
def create_world_02(request):
    return render(request, 'game/create_world02.html')

@login_required
def show_world_02(request):
    if "POST" == request.method:
        context = {}
        context['formData']  = yaml.load(request.POST.get("formData","No data found"),yaml.SafeLoader)
        world = b.get_world(request.user.get_username())
        world = the_second_age(world,context['formData'])
        #building a dictionairy in the format that d3.js will prefer
        wa = [world.df_features.loc[m].to_dict() for m in world.df_features.index]
        context['df_features'] = wa
        context['dim_1'] = np.unique(world.df_features['x']).tolist() 
        context['dim_2'] = np.unique(world.df_features['y']).tolist()
        return render(request,'game/show_world02.html',context)
    else:
        return render(request, 'game/create_world02.html')
