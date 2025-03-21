from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request,'recipes/page/home.html',context={
        'name': 'Samuel Oliveira'
    })
