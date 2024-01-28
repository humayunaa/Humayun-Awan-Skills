# simple_test_root/pages/views.py
from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#    return HttpResponse("Simple Test Site")

def index(request):
    return HttpResponse("<title>Humayun's First Django Page</title> <h1>Humayun Awan</h1> <h2>22373636</h2> <p>Humayun thinks django is a useful tool but can at times be a hassle with errors</p> <p>Humayun is excited to use django and to see how much he can accomplish with it</p>")
