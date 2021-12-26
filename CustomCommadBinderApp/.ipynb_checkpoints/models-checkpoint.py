from django.db import models

# Create your models here.
class Employee(models.Model):
    empchoice=(
        ("Employee","EM"),
        ("Manager","MG"),
    )
    eno=models.IntegerField()
    ename=models.CharField(max_length=255)
    edept=models.CharField(max_length=10,choices=empchoice)
    eactive=models.BooleanField()
    
    def __str__(self):
        return self.ename
   
    