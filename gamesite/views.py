from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.template import loader


# Create your views here.
from django.http import HttpResponse

from .lib import blogs
from .forms import SignUpForm


def index(request):
    carosel_items = []
    template = loader.get_template('prodweb/index.html')
    notebooks = blogs.get_notebooks_as_content()
    for notebook in notebooks:
        carosel_items.append({"title":notebook['title'],
            "subtext":notebook['subtext'],
            "link":notebook['filename'],
            "type":notebook['type']}) #currently the title and the link are the same thing. I might change this in the future. 
    context = {
        'articles':carosel_items,
        'notebooks':notebooks
    }    
    return render(request,'prodweb/index.html',context)


def notebook_article(request):
    notebooks = blogs.get_notebooks_as_content()
    fname = request.GET.get('article', 'article_not_found.html')
    if fname not in [i['filename'] for i in notebooks]:
        fname = 'article_not_found.html'
    article = "prodweb/notebooks/"+fname
    context = {"article":article}
    return render(request,'prodweb/jupyter_notebook.html',context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            returnApp = request.GET.get('next','/')
            return redirect(returnApp)
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def ads_text(request):
    return  render(request, 'prodweb/ads.txt')
