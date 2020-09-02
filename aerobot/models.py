from django.db import models

class ContactForm(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=50, null=True)
    message = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'ContactForm'
        verbose_name_plural = 'ContactForms'


class Sponsers(models.Model):
    name = models.CharField(max_length=100, null=True)
    link = models.CharField(max_length=10000,null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Sponsers'
        verbose_name_plural = 'Sponsers'


class Gallery(models.Model):
    link = models.CharField(max_length=100000000,null=True)

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'