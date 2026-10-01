from django.shortcuts import render
from django.shortcuts import redirect
from .models import Students
# Create your views here.
def home(request):
    solution=""
    if request.method=="POST":
        a=float(request.POST.get("a"))
        b=float(request.POST.get("b"))
        opr=request.POST.get("opr")
        if opr=="+":
            solution=a+b
        elif opr=="-":
            solution=a-b
        elif opr=="*":
            solution=a*b
        elif opr=="/":
            solution=a/b
        elif opr=="**":
                solution=a**b
        else:
             solution="Invalid Operation"
    return render(request,'index.html',{"solution":solution})



def student_form(request):
    message=""
    if request.method=="POST":
        Students.objects.create(
            name=request.POST['name'],
            rollno=request.POST['roll'],
            student_class=request.POST['class'],
            age=request.POST['age'],
            parentno=request.POST['contact']
        )
        message="student added successfully"
    return render(request,'student_form.html',{'message':message})


def student_list(request):
     students=Students.objects.all()
     return render(request,'student_list.html',{'students':students})

def student_update(request,id):
     student=Students.objects.get(id=id)
     if request.method=="POST":
          student.name=request.POST['name']
          student.rollno=request.POST['roll']
          student.student_class=request.POST['class']
          student.age=request.POST['age']
          student.parentno=request.POST['contact']
          student.save()
          return redirect('/modelsapp/list/')        
     return render(request,'student_update.html',{'student':student})

def student_delete(request,id):
     student=Students.objects.get(id=id)
     student.delete()
     return redirect('/modelsapp/list/')
