# Adventures in Data Science: an RPG built from the data science toolkit
**always a work in progress**
I'm still migrating a lot from my old flaskapp so I don't have a working demo online yet. I'll post the link here when I have it. 

## Django
The core app is written using Django. You can clone this app directly into your functioning Django app by:
```
urlpatterns = [
        path('game', include('game.urls')),
    ]
```

Note you'll need the standard login forms to authenticate the user where required. 

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

