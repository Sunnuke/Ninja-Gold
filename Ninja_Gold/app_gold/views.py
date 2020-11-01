from django.shortcuts import render, HttpResponse, redirect
import random
# Create your views here.
def index(request):
    if 'views' in request.session:
        request.session['views'] += 1
    else:
        request.session['views'] = 1
        request.session['userTotal'] = 0
        request.session['history'] = ''
    return render(request, 'index.html')

def process_money(request):
    # farm
    if int(request.POST['findGold']) == 1:
        print('farm')
        goldFound = random.randint(10,20)
        print(goldFound)
        request.session['userTotal'] += goldFound
    # cave
    if int(request.POST['findGold']) == 2:
        print('cave')
        goldFound = random.randint(5,10)
        print(goldFound)
        request.session['userTotal'] += goldFound
    # house
    if int(request.POST['findGold']) == 3:
        print('house')
        goldFound = random.randint(2,5)
        print(goldFound)
        request.session['userTotal'] += goldFound
    # casino
    if int(request.POST['findGold']) == 4:
        print('casino')
        goldFound = random.randint(0,50)
        print(goldFound)
        request.session['userTotal'] += goldFound
    return redirect('/')