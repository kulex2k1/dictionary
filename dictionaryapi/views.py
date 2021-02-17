from django.shortcuts import render, redirect
import requests
import json
from .forms import DictForm

# Create your views here."startdate":"2021-01-25", "enddate":"2021-02-08"


def index3(request): 
    
    if request.method == 'POST':
        #entry = request.POST.get('word')
        startdate = '2021-01-25'
        enddate = "2021-02-08"
        password ='b5553e79-23a6-42c8-90f6-988b72a29a4d'
        api_request = requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+ entry +'?key='+ password)
    try:
        api = json.loads(api_request.content)
        
    except Exception as e:
        raise Exception('Word not Found')

    context = {'api':api, 'entry': entry}
    return render(request, 'index.html', context)



def index(request):   
    if request.method == 'GET':
        entry = 'dictionary'
        password ='b5553e79-23a6-42c8-90f6-988b72a29a4d'
        api_request = requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+ entry +'?key='+ password)
    else:
        entry = request.POST.get('word')
        password ='b5553e79-23a6-42c8-90f6-988b72a29a4d'
        api_request = requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+ entry +'?key='+ password)
    
    try:
        api = json.loads(api_request.content)
    except Exception as e:
        raise Exception('Word not Found')

    context = {'api':api, 'entry': entry}
    return render(request, 'index.html', context)