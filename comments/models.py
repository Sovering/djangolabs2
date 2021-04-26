from django.db import models
from django.urls import reverse

# Create your models here.

class ServMonitor(models.Model):
    name = models.CharField("Имя", max_length=150)
    time = models.TimeField()
    type = models.CharField("Тип оповещения", max_length=150)
    email = models.EmailField()
    group = models.CharField("Группа серверов", max_length=150)
    group_type = models.CharField("Тип группы серверов", max_length=150)
    gps = models.GenericIPAddressField()
    url = models.SlugField(max_length=160, unique=True, null=False)
    draft = models.BooleanField("Черновик", default=False)


    def get_absolute_url(self):
        return reverse("serv_mon_detail", kwargs={"slug": self.url})


    def __str__(self):
        return self.name


class PdfMaker(models.Model):
    name = models.CharField("Имя", max_length=150)
    time = models.TimeField()
    type = models.CharField("Тип оповещения", max_length=150)
    email = models.EmailField()
    url = models.SlugField(max_length=160, unique=True, null=False)

    def get_absolute_pdf_url(self):
        return reverse("pdf_detail", kwargs={"slug": self.url})

    '''def get_absolute_pdf_export_url(self):
        return reverse("pdf_export", kwargs={"slug": self.url})'''

    def __str__(self):
        return self.name
