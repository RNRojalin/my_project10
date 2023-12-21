from django.shortcuts import render

# Create your views here.
def Myntra(request):
    return render(request,'Myntra.html')

def Urbanic(request):
    return render(request,'Urbanic.html')