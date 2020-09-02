from django.shortcuts import render
from .models import ContactForm, Sponsers, Gallery
from django.http import JsonResponse, HttpResponse
import json

def home(request):
    template = 'aerobot/sample.html'
    sponsers = Sponsers.objects.all()
    context = {'sponsers': sponsers}
    return render(request, template, context)


def about(request):
    template = 'aerobot/about.html'
    context = {}
    return render(request, template, context)

def gallery(request):
    gallery = Gallery.objects.all()
    template = 'aerobot/gallery.html'

    context = {'gallery': gallery}
    return render(request, template, context)

def blogs(request):
    template = 'aerobot/blogs.html'
    context = {}
    return render(request, template, context)

def contact(request):
    template = 'aerobot/contact.html'
    context = {}
    if request.is_ajax() and request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contactno = request.POST.get('contactno')
        msg = request.POST.get('msg')
        print(name)
        print(email)
        print(contactno)
        print(msg)
        form = ContactForm(name=name, email=email, phone_number=contactno, message=msg)
        form.save()
        data = {
            'message': 'Thanks We Will Get Back To You Soon !'
        }
        return HttpResponse(json.dumps(data), content_type='application/json')
    
    return render(request, template, context)            