from django.db import models

# Create your models here.



    
class Student(models.Model):
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=800)

    class Meta:
        app_label = 'authentication'

    