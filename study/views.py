from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def study3(request):
    return render(request,'study3.html')