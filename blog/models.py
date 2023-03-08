from django.db import models

from django.db.models.fields import CharField, URLField
from django.db.models.fields.files import ImageField

import datetime
# Create your models here.

#Aqui tan las publicaciones
class Post(models.Model):
    titulo = CharField(max_length=50)
    descripcion = models.TextField() #Quiero que sea un contenido largo, por eso text
    img = ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)