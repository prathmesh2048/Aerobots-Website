from django.db import models
from django.utils.text import slugify
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=2000)
    created = models.DateTimeField(default=timezone.now)
    image = models.CharField(max_length=10000,null=True)
    slug = models.SlugField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Blog, self).save(args, **kwargs)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name_plural = 'Blogs'
