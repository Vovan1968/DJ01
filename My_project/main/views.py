from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("<h1>My first project on Django</h1>")
def data(request):
    return HttpResponse("<h1>New page with data</h1>")
#def test(request):
   # return HttpResponse("<h1>New page for test</h1>")
def test(request):
    return render(request, 'test.html')
