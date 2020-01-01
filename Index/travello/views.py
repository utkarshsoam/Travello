from django.shortcuts import render
from .models import Destination
from django.core import serializers
from array import array


# Create your views here.
def index(request):

    #--------------STATIC WAY--------------------->

    # obj1=Destination()
    # obj1.name='Kashmir'
    # obj1.desc='The Place Where Soul Touch the Nature'
    # obj1.image='destination_1.jpg'
    # obj1.offer=True
    # obj1.price=700
    
    
    # obj2=Destination()
    # obj2.name='Shimla'
    # obj2.desc='See The Nature Beyound Your Imagination'
    # obj2.image='destination_2.jpg'
    # obj2.offer=False
    # obj2.price=750
    
    # obj3=Destination()
    # obj3.name='USA'
    # obj3.desc='We The Bold'
    # obj3.image='destination_3.jpg'
    # obj3.offer=True
    # obj3.price=850
    
    # obj4=Destination()
    # obj4.name='USA'
    # obj4.desc='We The Bold'
    # obj4.image='destination_3.jpg'
    # obj4.price=850

    # objecs = [obj1, obj2, obj3, ]
    # return render(request, "index.html", {'objec':objecs})

    #-------------Dynamic WAy from database----------------->

    objecs = Destination.objects.all()
    json_data = serializers.serialize("json",Destination.objects.all())    
    return render(request, "index.html", {'objec':objecs,'ob1' : json_data})

  


def banglore(request):
        
        return render(request, "banglore.html")

def mumbai(request):
        return render(request, "mumbai.html")        

def shimla(request):
        return render(request, "shimla.html") 

def bali(request):
        return render(request, "bali.html")

def goa(request):
        return render(request, "goa.html")                      

def gwalior(request):
        return render(request, "gwalior.html")          


def sea(request):
    if request.method == 'POST':
        city =request.POST[ 'city']
        city=city.upper()
        departure = request.POST[ 'departure']   
        arrival = request.POST[ 'arrival']   
        budget = request.POST[ 'budget'] 
        obj=Destination.objects.all()
        list=[]
        print(city)
        for obj1 in obj:
                if obj1.name == city:
                        list.append(obj1)
                        print(list)
                        return render(request, "index.html", {'objec':list})
      
    else:
        return render(request, 'index.html') 

       