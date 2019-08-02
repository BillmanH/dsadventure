from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import playerCharacterForm

from .lib.create_world import *
from .lib.modify_character import *

from .lib.boto import s3Transfer as b
import yaml

@login_required
def start_screen(request):
    return render(request,'game/start_screen.html')

@login_required
def core_view(request):
    context = {'charData':{},
            'mapData':{},
            'terrData':{}}
    world = b.get_world(request.user.get_username()) 
    return render(request, 'game/core_view.html',context)

@login_required
def create_character(request):
    if request.method == 'POST':
        form = playerCharacterForm(request.POST)
        if form.is_valid():
            #here is where all of the character creation will take place
            world = b.get_world(request.user.get_username()) 
            f = request.POST.dict()
            character_dict = {
                'name': f['name'],
                'background': dict(playerCharacterForm.backgroundChoices)[f['background']],
                'coreskills': dict(playerCharacterForm.coreSkillsChoices)[f['coreskills']],
                'secondaryskills': dict(playerCharacterForm.secondarySkillsChoices)[f['secondaryskills']]
            }
            world = create_character(character_dict,world)
        return HttpResponseRedirect('coreview')
    else:
        form = playerCharacterForm()
        return render(request, 'game/player/create.html', {'form': form})

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
        context = {'phase':1}
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
        context = {'phase':2}
        context['formData']  = yaml.load(request.POST.get("formData","No data found"),yaml.SafeLoader)
        world = b.get_world(request.user.get_username())
        world = the_second_age(world,context['formData'])
        #post the `world` to an s3 bucket, using the username as the key
        user = request.user.get_username()
        b.save_world(world,user)
        #After the world is saved we can change the df for display.   
        world.df_features = world.df_features.fillna('')
        #building a dictionairy in the format that d3.js will prefer
        wa = [world.df_features.loc[m].to_dict() for m in world.df_features.index]
        context['df_features'] = wa
        context['dim_1'] = np.unique(world.df_features['x']).tolist() 
        context['dim_2'] = np.unique(world.df_features['y']).tolist()
        return render(request,'game/show_world02.html',context)
    else:
        return render(request, 'game/create_world02.html')


@login_required
def show_world_03(request):
        context = {'phase':3}
        world = b.get_world(request.user.get_username())
        world,events = the_third_age(world)
        #post the `world` to an s3 bucket, using the username as the key
        user = request.user.get_username()
        b.save_world(world,user)
        #building a dictionairy in the format that d3.js will prefer
        context['events'] = events
        context['rulers'] = [str(n.ruler) for n in world.nations]
        context['loyalty'] = [str(n) for n in world.nations]
        return render(request,'game/show_world03.html',context)
