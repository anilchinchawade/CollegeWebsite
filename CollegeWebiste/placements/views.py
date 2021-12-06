from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from .models import Contact
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def services(request):
    return render(request,'services.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        emailid = request.POST.get('emailid')
        phoneno = request.POST.get('phoneno')
        remarks = request.POST.get('remarks')
        date = datetime.today()
        contact = Contact(name=name,emailid=emailid,phoneno=phoneno,remarks=remarks,date=date)
        contact.save()
        messages.success(request,"Your information and remarks have been reched to us!! Thank You!!! ")

    return render(request,'contact.html')


