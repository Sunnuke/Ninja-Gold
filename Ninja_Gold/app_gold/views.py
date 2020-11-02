from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime,localtime

# Create your views here.
def index(request):
    if 'views' not in request.session:
        request.session['views'] = 0
    if 'views' not in request.session:
        request.session['views'] = 0
    if 'userTotal' not in request.session:
        request.session['userTotal'] = 0
    if 'history' not in request.session:
        request.session['history'] = []
    if 'history' not in request.session:
        request.session['color'] = ""
    return render(request, 'index.html')

def process_money(request):
    time = {
        "time" : strftime(" %H:%M ", localtime()),
        "mdy": strftime(" %m/%d/%Y ", localtime())
    }
    # farm
    if int(request.POST['findGold']) == 1:
        request.session['color'] = "green"
        print('farm')
        goldFound = random.randint(10,20)
        print(goldFound)
        request.session['userTotal'] += goldFound
        act = f"Earned {goldFound} golds from farm! ({time['time']} {time['mdy']})"
        request.session['history'].insert(0, str(act))
        print(request.session['history'])
    # cave
    elif int(request.POST['findGold']) == 2:
        request.session['color'] = "green"
        print('cave')
        goldFound = random.randint(5,10)
        print(goldFound)
        request.session['userTotal'] += goldFound
        act = f"Earned {goldFound} golds from cave! ({time['time']} {time['mdy']})"
        request.session['history'].insert(0, str(act))
        print(request.session['history'])
    # house
    elif int(request.POST['findGold']) == 3:
        request.session['color'] = "green"
        print('house')
        goldFound = random.randint(2,5)
        print(goldFound)
        request.session['userTotal'] += goldFound
        act = f"Earned {goldFound} golds from house! ({time['time']} {time['mdy']})"
        request.session['history'].insert(0, str(act))
        print(request.session['history'])
    # casino
    elif int(request.POST['findGold']) == 4:
        print('casino')
        upOrdown = random.randint(1,2)
        if upOrdown == 1:
            request.session['color'] = "green"
            goldFound = random.randint(0,50)
            request.session['userTotal'] += goldFound
            print(goldFound)
            act = f"Entered a casino and Won {goldFound} golds! YAY! ({time['time']} {time['mdy']})"
            request.session['history'].insert(0, str(act))
            print(request.session['history'])
        else:
            request.session['color'] = "red"
            goldFound = random.randint(1,50)
            request.session['userTotal'] -= goldFound
            print('-',goldFound)
            act = f"Entered a casino and lost {goldFound} golds... Ouch! ({time['time']} {time['mdy']})"
            request.session['history'].insert(0, str(act))
            print(request.session['history'])
    return redirect('/')

