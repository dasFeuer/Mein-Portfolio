from django.shortcuts import render, HttpResponse

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
    # return HttpResponse("Kontaktseite (/contact)")
    return render(request, 'contact.html')


