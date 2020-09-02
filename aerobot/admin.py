from django.contrib import admin
from .models import ContactForm, Gallery, Sponsers
# Register your models here.
admin.site.register(ContactForm)
admin.site.register(Sponsers)
admin.site.register(Gallery)