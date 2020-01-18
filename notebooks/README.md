# notebooks are the best documentation
If you are looking to replicate, or clone anything. Checkout the `notebooks` folder.

__often times notebooks on GitHub don't load__ [Here is the link](http://williamjeffreyharding.com/blog/?article=Generating_a_Random_World_Map_in_Python.html&utm_source=github&utm_medium=readme&utm_campaign=blogs) to some of those notebooks on my personal blog.  
All backend functions are developed in Jupyter notebooks. The notebooks `import` the actual modules used in the production code. The only difference is that the notebooks provide a REPL run-through of each function so that it can be examined and documented. 

## Stages of the world generation process
* Geography - the creation of geological features and elevation.
* Cities and Nations - population, buildings and division into nation-states.
* Conflict - events and procedures that bring story to the world. 

### World Pickles
* worlds (and everything in them) are saved in `pickle` files (`p`)
actual user `world` objects are stored in `\pickles\` as `.pkl` rather than `p`. `p` is used for dev worlds that may not work in production. All pickles are in the `.gitignore`. However if you reach out to me via email I might send you the pickle of your saved game. 


### Each time you move from one place to annother:
@login_required
1. get the updated character data from the userform
```
        charData = yaml.load(request.POST['charData'])
```
2. get the old world (before the update)
```world = b.get_world(request.user.get_username())
context['old_location'] = world.Character.get_location_key()
```
3. update the charData with this function (keeps the update out of the users's hands)
```
world.Character = modify_character.update_charData(world,charData)\
```
4. the location is now where the character will be
```
new_location = world.Character.get_location_key()
world.Character.turn_number += 1
```
5. keeping track of whether or not the character has been there
```
world.df_features.loc[context['old_location'],'visited'] = 1
world.df_features.loc[context['old_location'],'aware'] = 1
world.df_features.loc[context['old_location'],'turn_last_visited'] = world.Character.turn_number
```
6. Save that pickle
```
save_world(world,request.user.get_username())
```
7. with the updated world, populate the context
```
context['areas_visited'] = world.df_features['visited'].sum()
context['charData'] = world.Character.get_charData()
context['terrData'] = world.df_features.loc[world.Character.get_location_key()].fillna("none").to_dict()
```
8. terrain details come from Azure SQL
```
tdt = terrain_details.objects.values().get(name=context['terrData']['terrain'])
```
9. terrain items for each item in the terrain textures. 

```
context['mapData'] = w.get_area_data(world)
```
* td is the lists of textures for the world, not the details
```
td = yaml.load(tdt['terrain_textures'],Loader=yaml.SafeLoader)
```
* ti is the list of items 
```
ti = [t['name'] for t in td]
tt = list(terrain_items.objects.values().filter(pk__in=ti))
```
* bundled into a dict for smooth loading
```
context['n_ter_items']=[
            {'texture':tt[i],
                'detail':[t for t in td if t['name'] == tt[i]['name']][0]
                } for i in range(len(tt))
            ]
``` 
10. once context is collected it can be modified with builder specific modifiers
```
if context['terrData']['terrain'] == 'town':
    context = builders.towns.modify_context(world,context) 
```
11. roll a die to dermine if monsters will show up in this worl. Add monsters to context if they do. 
```
if monsters.check_for_monsters(world):
    mi = tdt['creatures'].split(",") 
    m = list(bestiary.objects.values().filter(pk__in=mi))
    context['terrData']['monsters'] = m
    context = monsters.add_monsters_to_context(world,context)
```
12. changes and localization variables come last
```
context['charData']["current situation"] = w.get_character_context(world,context)
return render(request, 'game/core_view.html',context)
```