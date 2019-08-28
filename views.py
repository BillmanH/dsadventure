from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from .forms import playerCharacterForm

from .lib.create_world import *
from .lib.builders import world as w
from .lib import modify_character 

from .lib.boto import s3Transfer as b
import yaml

from .models import bestiary,terrain_details,terrain_items

@login_required
def start_screen(request):
    return render(request,'game/start_screen.html')

@login_required
def core_view(request):
    """
    b = loading and saving functions
    w = world module
    """
    context = {}
    if "POST" == request.method:
        #get the updated character data from the userform
        charData = yaml.load(request.POST['charData'])
        #get the old world (before the update)
        world = b.get_world(request.user.get_username())
        context['old_location'] = world.Character.get_location_key()
        #update the charData with this function (keeps the update out of the users's hands)
        world.Character = modify_character.update_charData(world,charData)
        new_location = world.Character.get_location_key()
        if 'visited' not in world.df_features.columns:
            world.df_features.loc[context['old_location'],'visited'] = 1
        world.df_features.loc[context['old_location'],'visited'] = 1
        b.save_world(world,request.user.get_username())
        #with the updated world, populate the context
    if "GET" == request.method:
        #world objects come from pickles, loaded from s3
        world = b.get_world(request.user.get_username())
    context['worlds_visited'] = world.df_features['visited'].sum()
    #in bost POST(traveling) or GET(loading) the context is populated in the same way.
    context['charData'] = world.Character.get_charData()
    if 'old_location' in context.keys():
        context['charData']['old_location'] = context['old_location']
    context['terrData'] = world.df_features.loc[world.Character.get_location_key()].fillna("none").to_dict()
    #terrain details come from Azure SQL
    td = terrain_details.objects.values().get(name=context['terrData']['terrain'])
    #terrain items for each item in the terrain textures. 
    context['mapData'] = w.get_area_data(world)
    #td is the lists of textures for the world, not the details
    td = yaml.load(td['terrain_textures'],Loader=yaml.SafeLoader)
    #ti is the ist of items 
    ti = [t['name'] for t in td]
    tt = list(terrain_items.objects.values().filter(pk__in=ti))
    #bundled into a dict for smooth loading
    context['n_ter_items']=[
            {'texture':tt[i],
                'detail':[t for t in td if t['name'] == tt[i]['name']][0]
                } for i in range(len(tt))
            ]
    #changes and localization variables come last
    context['charData']["current situation"] = w.get_character_context(world)
    return render(request, 'game/core_view.html',context)

@login_required
def char_map(request):
    context = {}
    world = b.get_world(request.user.get_username())
    #building a dictionairy in the format that d3.js will prefer'
    masked_world = w.mask_unknown(world)
    wa = [masked_world.loc[m].fillna("").to_dict() for m in world.df_features.index]
    context['df_features'] = wa
    context['dim_1'] = np.unique(world.df_features['x']).tolist() 
    context['dim_2'] = np.unique(world.df_features['y']).tolist()
    context['charData'] = world.Character.get_charData()
    return render(request, 'game/char_map.html',context)

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
            world = modify_character.create_character(character_dict,world)
            b.save_world(world,request.user.get_username())
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
