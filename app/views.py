from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO = TopicForm()
    d = {'ETFO':ETFO}
    if request.method == 'POST':
        TFDO = TopicForm(request.POST)
        if TFDO.is_valid():
            tn = TFDO.cleaned_data['topic_name']
            TO = Topic.objects.get_or_create(topic_name = tn)[0]
            TO.save()
            return HttpResponse('Data inserted...')
        else:
            return HttpResponse('Data inserted is invalid..')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO = WebpageForm()
    d = {'EWFO':EWFO}
    if request.method == 'POST':
        WFDO = WebpageForm(request.POST)
        if WFDO.is_valid():
            tn = WFDO.cleaned_data['topic_name']
            TO = Topic.objects.get(topic_name = tn)
            n = WFDO.cleaned_data['name']
            u = WFDO.cleaned_data['url']
            e = WFDO.cleaned_data['email']
            WO = Webpage.objects.get_or_create(topic_name = TO,name = n,url = u,email = e)[0]
            WO.save()
            return HttpResponse('Webpage Inserted')
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    EAFO = AccessRecordForm()
    d = {'EAFO':EAFO}
    if request.method == 'POST':
        AFDO = AccessRecordForm(request)
        if AFDO.is_valid():
            n = AFDO.cleaned_data['name']
            WO = Webpage.objects.get(name = n)
            d = AFDO.cleaned_data['']
    return render(request,'insert_access.html',d)