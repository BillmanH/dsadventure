# Adventures in Data Science: an RPG built from the data science toolkit
**always a work in progress**
I'm still migrating a lot from my old flaskapp so I don't have a working demo online yet. I'll post the link here when I have it. 

# Infrastructure
## Django
The core app is written using Django. You can clone this app directly into your functioning Django project by cloning this repo into your project directory and adding the URLs to your production urls.py view. The totorial on the django website should show you how to use this.

Example snippet to add to your urls.py:
```
urlpatterns = [
        path('game', include('game.urls')),
    ]
```

You will also need:
* settup for authentication
* a sql-like database (I'm using Azure SQL even though the app is hosted on EC2) 

have a look at the [conda env](https://github.com/BillmanH/homepage/blob/master/prodweb_env.yaml) for more clues.
## Jupyter Notebooks
Notebooks can be served via ssh forwarding. This allows me to test and tinker with the actual deployed code without disrupting the live server. All functions run out of those notebooks are the same as they are in the live app.

Notebooks also serve as tests for the logic in the apps. When making changes you can run all of the notebooks to ensure that they complete. 

## Scikit Learn
This is used to:
* Calculate the area of nation states
## Pandas and Numpy
* most maps are created in DataFrame objects
* random number and matrix manipulation is done using numpy tools
## D3.js
Visuals in notebooks are done using Altair, however the core web UI is all built in D3.js. 

# generation parameters
The world is generated randomly based on a number of features that the user dicides such as mountain height, average rainfall, number of nation or cities. Then everythign is spun up each time a new game begins. 

### parameters that shape the world
Each of these takes an optional argument `params` which customizes the world. Default parameters are defined in the `__init__` function of each module.  
* landscape = contains everything about the natural features of the world.
* culture = contains everyting relating to the things built by civilizations such as people and towns. 

There are specific modules for `nations`, `towns`, and `people` that all take imput from either `landscape` or `culture`. All outputs should end up in the **`world`** object. 
