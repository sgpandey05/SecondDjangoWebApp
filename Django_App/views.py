from django.shortcuts import render, HttpResponse, redirect
from Django_App.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context ={
        'name':'shivam',
        'surname':'pandey'
    }
    # return HttpResponse('home page')
    # return render(request,'index.html')
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')
    # return HttpResponse('about page')
def services(request):
    return render(request,'services.html')
    # return HttpResponse('services page')
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone') 
        password = request.POST.get('password')
        contact = Contact(name = name, email= email, phone = phone , password = password)
        # contact = Contact(name = name, email= email, phone = phone , password = password)
        contact.save()
        messages.success(request, 'Profile details updated.')

    return render(request,'contact.html')
    # return HttpResponse('contact page')
     
def login(request):
    return render(request,'login.html')

def logout(request):
    return render(request,'index.html')