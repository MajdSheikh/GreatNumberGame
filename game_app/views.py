from urllib import request
from django.shortcuts import render
import random


def index(request):
    del request.session['number']
    if 'number' not in request.session:
        request.session['message']= " "
        request.session['number'] = random.randint(1, 100)
    print(request.session['number'])
    return render(request,'index.html')

def method2(request):
    x = int(request.POST['number'])
    if x < request.session['number']:
        request.session['message'] = "toolow"
    elif x > request.session['number']:
        request.session['message'] = "toohigh"
    else:
         request.session['message'] = "equal"
    return render(request, 'index.html')


