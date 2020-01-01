from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#  py .\manage.py runserver  (command to run the server)
def home(request):
    return render(request,'home.html',{'name':'Utkarsh Soam'})   #<-----Dictionary

def Add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res = val1 + val2
    return render(request,'result.html',{'result':res})   