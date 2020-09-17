from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mypersonalportfolio1/home.html') 
    