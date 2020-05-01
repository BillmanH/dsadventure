# Adventures in Data Science: an RPG built from the data science toolkit
**always a work in progress**


![Alt text](/docs/screenshot_start.png?raw=true "overland map")


The core application is functional, but still has a long way to go before I have a _game_. I'm not guaranteeing that I'll keep it online 24/7 as I'm actively building it out. I'm not even at the point where I'm posting the game link. PM me if you want to see it in action though. 

# How to play:
## Create a world (you'll need to create an account)
The world you create is your own. It's your own saved world with its own history, people and problems. In the creation phase you can tweak the parameters of the world to make the world that you want to play in. 

![Alt text](/docs/screenshot_map.png?raw=true "overland map")

## Create a character
Choose the starting characteristics. You will start with the most basic skills and gear; you will have to find out how to get better skills and gear.

![Alt text](/docs/Screenshot_moutnain.png?raw=true "overland map")


## Have adventures
* Killing monsters out in the world makes the world safer, and people like you more.
    * plus you might get some cool loot.


![Alt text](/docs/screeshot_forest.png?raw=true "overland map")


# Infrastructure
## Django
The core app is written using Django. You can clone this app directly into your existing Django project by cloning this repo into your project directory and adding the URLs to your production urls.py view. The tutorial on the Django website should show you how create a Django project if you don't have one.

Example snippet to add to your `urlpatterns` in your `urls.py`:
```
urlpatterns = [
        path('game', include('game.urls')),
    ]
```

Also add this to your `INSTALLED_APPS` in your `settings.py`
```
INSTALLED_APPS = [
    'game.apps.gameConfig'
    ]
```
**note** that I'm using `game` as the cloned repository folder, which may be different than the name of this repository. If you cloned your repository under a different name, then you need to change `game` to your git rep folder name.

You will also need:
* setup for authentication (mine is in the main prodweb django project, not this app)
        * You couldn't just remove the `@login_required` decorators as the app uses the user accounts to get the custom world for each user. 
* a sql-like database (I'm using Azure SQL even though the app is hosted on EC2), but the default sql-lite should work fine.
    * you will need to migrate your model to the db on your initial setup. See Django docs on doing this.
* Google analytics tags, but that's easy to just remove if you don't want it. 

have a look at the [conda env](https://github.com/BillmanH/homepage/blob/master/prodweb_env.yaml) for more clues.
## Jupyter Notebooks
Notebooks can be served via ssh forwarding. This allows me to test and tinker with the actual deployed code without disrupting the live server. All functions run out of those notebooks are the same as they are in the live app. Notebooks also serve as tests for the logic in the apps. When making changes you can run all the notebooks to ensure that they complete. 

You can see the notebooks in the `notebooks` folder, but my favorites are also posted [on my personal blog](http://williamjeffreyharding.com/blog/?article=Generating_a_Random_World_Map_in_Python.html&utm_source=github&utm_medium=readme&utm_campaign=blogs) , **which is offline right now due to COVID**

## Scikit Learn
This is used to:
* Calculate the area of nation states
## Pandas and Numpy
* most maps are created in DataFrame objects
* random number and matrix manipulation are done using numpy tools
## D3.js
Visuals in notebooks are done using Altair, however the core web UI is all built in D3.js. 

# generation parameters
The world is generated randomly based on several features that the user decides such as mountain height, average rainfall, number of nation or cities. Then everything is spun up each time a new game begins. 

### parameters that shape the world
Each of these takes an optional argument `params` which customizes the world. Default parameters are defined in the `__init__` function of each module.  
* landscape = contains everything about the natural features of the world.
* culture = contains everything relating to the things built by civilizations such as people and towns. 

There are specific modules for `nations`, `towns`, and `people` that all take input from either `landscape` or `culture`. All outputs should end up in the **`world`** object.

### object hierarchy:
world
* culture - json dict of attributes that affect how people behave, used in `Person.__init__()` functions
* landscape - json dict used in shaping terrain
* nations - list of `Nation` objects
* towns - list of `Town` objects
* people - list of `Person` objects
* df_features - `pandas.dataframe` of terrain squares
* Character - the player character object, equipment and experience


### TODO: Ideas that I have, jot them down quickly so that I can think of them later. 
* Time advances in a weekly manner
    * Has seasons
    * Add snow to terrain in wintertime
* Population birthrate is set to sum of danger area surrounding town. 
