from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Sdetails
from django.db import IntegrityError
from django.contrib import messages

# Create your views here.
def hello(request):
    return HttpResponse('Hello this is student hello view 👨🏻‍🎓')

def sform(request):
    if request.method == 'POST':
        roll_no = request.POST.get('roll_no')
        st_name = request.POST.get('st_name')
        age = request.POST.get('age')
        email = request.POST.get('email')
        branch = request.POST.get('branch')

        if Sdetails.objects.filter(roll_no = roll_no):
            messages.error(request, "Roll number you entered already exists!")
            return redirect('sform')

        if Sdetails.objects.filter(email = email):
            messages.error(request, "Email you entered already exists!")
            return redirect('sform')
        
        Sdetails.objects.create(
            roll_no = roll_no,
            st_name = st_name,
            age = age,
            email = email,
            branch = branch
        )
        messages.success(request, "Student registered successfully!")
        return redirect('sdetails')

    return render(request,'sform.html')

def sall(request):
    all = Sdetails.objects.all()
    return render(request,'sdetails.html',{'all':all})

def sdel(request, id):
    d = Sdetails.objects.get(id=id)
    d.delete()
    return redirect('sdetails')

def supdate(request, id):
    student = Sdetails.objects.get(id=id)
    if request.method == 'POST':
        student.roll_no = request.POST.get('roll_no')
        student.st_name = request.POST.get('st_name')
        student.age = request.POST.get('age')
        student.email = request.POST.get('email')
        student.branch = request.POST.get('branch')
        student.save()
        return redirect('sdetails')
    return render(request, 'sform.html', {'student': student})