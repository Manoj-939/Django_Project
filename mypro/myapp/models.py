from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField(max_length=100)
    rollno=models.IntegerField(unique=True)
    age=models.IntegerField()
    student_class=models.IntegerField()
    parentno=models.CharField(max_length=15)

    def __str__(self):
     return f"{self.rollno} - {self.name}"