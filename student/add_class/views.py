from django.shortcuts import render, redirect
from add_class.models import StuClassName, StudentInfo
from add_class.forms import AddClass, StudentData

# Create your views here.
def class_add(request):
    class_form = AddClass(request.POST or None)
    print(class_form)
    if request.method == 'POST':
        if class_form.is_valid():
            class_form.save()
            return redirect('/')
    context = {
        'class_form': class_form,
        
    }
    return render(request, 'index.html', context)

def add_student_data(request):
   
    stu_form = StudentData(request.POST or None)
    if request.method == 'POST':
        if stu_form.is_valid():
            print(stu_form)
            stu_form.save()
        return redirect('/')
    context = {
        'stu_form': stu_form    
    }
    return render(request, 'add_student.html', context)
