from django.shortcuts import render
# Create your views here.

def index(request):
    x = {'name' : 'mostafa' , 'age' : 20}
    return render(request,'pages/index.html',x)

def about(request):
    return render(request,'pages/about.html')
