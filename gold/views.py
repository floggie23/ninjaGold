from django.shortcuts import render
from django.shortcuts import render, HttpResponse , redirect
import random 
import datetime
def index(request):
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'current_coins' not in  request.session:
        request.session['current_coins'] = 0
    return render(request,'index.html')
def take(request,place):
    get_coin = 0
    if place == 'farm':
        get_coin += random.randrange(10, 15)
        request.session['current_coins'] += get_coin
    elif place == 'cave':
        get_coin += random.randrange(10, 15)
        request.session['current_coins'] += get_coin
    elif place == 'house':
        get_coin += random.randrange(10, 15)
        request.session['current_coins'] += get_coin
    else:
        if place == 'casino':
            get_coin += random.randrange(-50, 50)
            request.session['current_coins'] += get_coin
    now = datetime.datetime.now()
    time=now.strftime("%Y-%m-%d %H:%M:%S")
    if get_coin > 0:
        request.session['activities'].append({
            'activity': "Earned",
            'gold' : get_coin,
            'place' : f"from { get_coin }!" ,
            'time' : time,
            'color' : "green"

        })
    else:
        request.session['activities'].append({
            'activity': f"Entered a casino and lost { get_coin }...Ouch", 
            'time' : time,
            'color': "red"

        })
    response = redirect('/')
    return response


