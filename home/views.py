from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("Mein Portfolio (/)")
    context = {'name': 'Barun', 'level': 'beginner'}
    return render(request, 'home.html', context)

def about(request):
    # return HttpResponse(" Info-Seite(/about)")
    return render(request, 'about.html')


def projects(request):
    # return HttpResponse(" Projektseite (/projects)")
    return render(request, 'projects.html')


def contact(request):
     if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        # print(name, email, phone, desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        print("The data has been written to the database.")
    # return HttpResponse("Kontaktseite (/contact)")
     return render(request, 'contact.html')


