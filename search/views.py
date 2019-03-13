from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

# Create your views here.


def index(request):
    students = Student.objects.all()
    return render(request, 'search/index.html', {'students': students})


def add(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('search:index')
            except:
                pass
    else:
        form = StudentForm()
    
    return render(request, 'search/add.html', {'form': form})

def view(request,roll):
    student = Student.objects.get(roll=roll)  
    return render(request,'search/view.html', {'st':student})  