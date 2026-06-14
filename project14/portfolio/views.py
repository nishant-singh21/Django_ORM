from django.shortcuts import render
from .models import Student


def student_list(request):
    students = Student.objects.all()
    return render(request, 'portfolio/student_list.html', {'students': students})

# {'students': students} this is a context dictionary that is passed to the template. It allows the template to
#  access the list of students and display them accordingly.
