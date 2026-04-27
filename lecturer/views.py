from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Ldetails
from django.db import IntegrityError

# Create your views here.
def hello(request):
    return HttpResponse('Hello this is lecturers hello view 👨🏻‍🎓')

def lform(request):
    if request.method == 'POST':
        try:
            l_id = request.POST.get('l_id')
            l_name = request.POST.get('l_name')
            l_email = request.POST.get('l_email')
            l_subject = request.POST.get('l_subject')

            Ldetails.objects.create(
                l_id=l_id,
                l_name=l_name,
                l_email=l_email,
                l_subject=l_subject
            )

            return redirect('ldetails')

        except IntegrityError:
            return HttpResponse("The ID or email you entered already exists!")

    return render(request, 'lform.html')

def lall(request):
    all = Ldetails.objects.all()
    return render(request,'ldetails.html',{'all':all})

def ldel(request,id):
    d = Ldetails.objects.get(id=id)
    d.delete()
    return redirect('ldetails')

def lupdate(request, id):
    lecturer = Ldetails.objects.get(id=id)
    if request.method == 'POST':
        lecturer.l_id = request.POST.get('l_id')
        lecturer.l_name = request.POST.get('l_name')
        lecturer.l_email = request.POST.get('l_email')
        lecturer.l_subject = request.POST.get('l_subject')
        lecturer.save()
        return redirect('ldetails')
    return render(request, 'lform.html', {'lecturer': lecturer})