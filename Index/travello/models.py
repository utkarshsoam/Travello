from django.db import models

# Create your models here.

# class Destination:
#     id:int
#     name:str
#     image:str
#     desc:str
#     price:int
#     offer:bool

    #Model
class Destination(models.Model):
    
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    url = models.CharField(max_length=100)

    #to create the table in the dtabase we have to migrate our model to databse by using the following command
                        #python manage.py makemigration
                        #python manage.py migrate(re-migration)