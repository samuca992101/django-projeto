from django.shortcuts import render
# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(request):
    return render(request,'recipes/home.html',context={
        'name': 'Samuel Oliveira'
    })
def Contato(request):
    return render(request, 'me-apague/temp.html')
def Sobre(request):
    return HttpResponse('sobre')