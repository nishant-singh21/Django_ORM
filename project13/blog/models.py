from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    enrollment_date = models.DateField(auto_now_add=True)

    # def __str__(self):
    #     return self.name
