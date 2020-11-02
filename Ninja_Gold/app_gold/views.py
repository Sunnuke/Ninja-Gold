from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime,localtime

# Create your views here.
def index(request):
    request.session['turns'] -= 1
    # dictionary = request.POST
    # print(dictionary)
    # amount = dictionary['goals']
    # turns = dictionary['turns']
    # print(amount, turns)
    # request.session['goals'] = amount
    # request.session['turns'] = turns
    if 'userTotal' not in request.session:
        request.session['userTotal'] = 0
    if 'history' not in request.session:
        request.session['history'] = []
    if 'history' not in request.session:
        request.session['color'] = ""
    print("goals: ", request.session['goals'], "turns: ", request.session['turns'])
    return render(request, 'index.html')

def process_money(request):
    time = {
        "time" : strftime(" %H:%M ", localtime()),
        "mdy": strftime(" %m/%d/%Y ", localtime())
    }

    if request.session['userTotal'] >= request.session['goals']:
        return render(request, 'win.html')

    elif request.session['turns'] <= 0:
        return render(request, 'lost.html')

    # farm
    elif int(request.POST['findGold']) == 1:
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
        upOrdown = random.randint(1,4)
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
    return redirect('/game')


# RESET
def reset(request):
    del request.session['goals']
    del request.session['turns']
    request.session['userTotal'] = 0
    request.session['history'] = []
    request.session['color'] = ""
    return redirect('/')

#USER GOALS
def goals(request):
    print(request.POST)
    if 'goals' not in request.session:
        request.session['goals'] = 0
        request.session['turns'] = 0
    # if 'goals' in request.session or 'turns' in request.session:
    #     request.session['goals'] = request.POST['goals']
    #     request.session['turns'] = request.POST['turns']
    # else:
    #     request.session['goals'] = request.POST['goals']
    #     request.session['turns'] = request.POST['turns']
    print("goals: ", request.session['goals'], "turns: ", request.session['turns'])
    # request.session['goals'] = request.POST['goals']
    # request.session['turns'] = request.POST['turns']
    return render(request, 'goals.html')

def process(request):
    request.session['goals'] += int(request.POST['goals'])
    request.session['turns'] += int(request.POST['turns'])
    request.session['turns'] += 1
    return redirect('/game')
