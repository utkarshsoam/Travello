from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('banglore',views.banglore, name='banglore'),
    path('mumbai',views.mumbai, name='mumbai'),
    path('shimla',views.shimla, name='shimla'),
    path('bali',views.bali, name='bali'),
    path('goa',views.goa, name='goa'),
    path('gwalior',views.gwalior, name='gwalior'),
    path("sea",views.sea, name='sea'),

 

]