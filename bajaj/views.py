from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse

def discovary(request):
    return HttpResponse('if u buy the bike prophit for u')