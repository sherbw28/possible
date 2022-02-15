from unicodedata import name
from django.shortcuts import render, redirect
from .models import Play, Eat, TypeOfPlace, PrefeCode,Atmosphere
from .forms import PlayForm, EatForm, TypeOfPlaceForm
import random
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin

def index(request):
    return render(request, 'testRoot/index.html')

def list_play(request):
    lists = Play.objects.filter(pk=1)
    content = {
        'lists': lists
    }
    
    return render(request, 'testRoot/list_play.html', content)

def list_eat(request):
    x = random.randint(1,6)
    lists = Eat.objects.filter(pk=x)
    content = {
        'lists': lists
    }
    
    return render(request, 'testRoot/list_eat.html', content)

def test(request):
    return render(request, 'testRoot/test.html')

def list_all(request):
    lists_test_play = TypeOfPlace.objects.filter(type="play")
    lists_test_eat = TypeOfPlace.objects.filter(type="eat")
    
    a = random.randint(0,len(lists_test_play) - 1)
    b = random.randint(0,len(lists_test_eat) - 1)
    c = random.randint(0,len(lists_test_play) - 1)
        
    while a == c:
        c = random.randint(0,len(lists_test_play))
        
    for i, list in enumerate(lists_test_play):
        print(i)
        if i == a:
            list_test_1 = list
        if i == c:
            list_test_3 = list
            
    for i, list in enumerate(lists_test_eat):
        if i == b:
            list_test_2 = list
            
    lists_test = [list_test_1,list_test_2,list_test_3]
    
    content = {
        'lists_test': lists_test
    }
    return render(request, 'testRoot/list_all.html', content)

def test_direction(request):
    return render(request, 'testRoot/test_direction.html')


def test1(request): 
    if request.method == 'POST':
        # area = request.POST.get("area")
        prefs = request.POST.getlist("pref")
        atmos = request.POST.get('atm')
        if len(prefs) == 0:
            return render(request, 'testRoot/index.html')
        if atmos == 'all':
            lists_test_play = TypeOfPlace.objects.filter(type="play").filter(pref__name__in=prefs)
            lists_test_eat = TypeOfPlace.objects.filter(type="eat").filter(pref__name__in=prefs)
        else:
            lists_test_play = TypeOfPlace.objects.filter(type="play").filter(pref__name__in=prefs).filter(atmosphere__type=atmos)
            lists_test_eat = TypeOfPlace.objects.filter(type="eat").filter(pref__name__in=prefs).filter(atmosphere__type=atmos)
            
        if (len(lists_test_play) < 2) or (len(lists_test_eat) < 1):
            return render(request, 'testRoot/index.html')
        
    else:
        lists_test_play = TypeOfPlace.objects.filter(type="play")
        lists_test_eat = TypeOfPlace.objects.filter(type="eat")
        
    a = random.randint(0,len(lists_test_play) - 1)
    b = random.randint(0,len(lists_test_eat) - 1)
    c = random.randint(0,len(lists_test_play) - 1)
            
    while a == c:
        c = random.randint(0,len(lists_test_play))
            
    for i, list in enumerate(lists_test_play):
        if i == a:
            list_test_1 = list
            ido1 = list.ido
            keido1 = list.keido
        if i == c:
            list_test_3 = list
            ido3 = list.ido
            keido3 = list.keido
            
    for i, list in enumerate(lists_test_eat):
        if i == b:
            list_test_2 = list
            ido2 = list.ido
            keido2 = list.keido
                
    lists = [list_test_1, list_test_2, list_test_3] 
        
    content = {
        'ido1':ido1,
        'keido1':keido1,
        'ido2':ido2,
        'keido2':keido2,
        'ido3':ido3,
        'keido3':keido3,
        'lists': lists
    }
    return render(request, 'testRoot/test1.html', content)

def test2(request):
    if request.method == "POST":
        form = TypeOfPlaceForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('index')
    else:
        form = TypeOfPlaceForm()
    return render(request, 'testRoot/test2.html', {'form': form})

def test3(request):
    return render(request, 'testRoot/test3.html')

def test4(request):
    return render(request, 'testRoot/test4.html')

def test5(request):
    return render(request, 'testRoot/test5.html')

def rootDisplay(request):
    lists_play = Play.objects.all()
    lists_eat = Eat.objects.all()
    x = random.randint(1,len(lists_play))
    y = random.randint(1,len(lists_eat))
    z = random.randint(1,len(lists_play))
    while x == z:
        z = random.randint(1,len(lists_play))
        
    list_1 = Play.objects.filter(pk=x)
    list_2 = Eat.objects.filter(pk=y)
    list_3 = Play.objects.filter(pk=z)
    lists = [list_1, list_2, list_3]
    
    
    for i, list in enumerate(lists):
        for date in list:
            if i == 0:
                address1 = date.address
            elif i == 1:
                address2 = date.address
            else:
                address3 = date.address
    
    
    
    content = {
        'address1': address1,
        'address2': address2,
        'address3': address3,
        'lists': lists
    }
    
    return render(request, 'testRoot/rootDisplay.html', content)