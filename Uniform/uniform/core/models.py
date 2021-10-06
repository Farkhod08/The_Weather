from django.db import models


class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "Biz xaqimizda"
        verbose_name_plural = "Biz xaqimizda"

    def __str__(self):
        return "Biz xaqimizda"


# Servise Xizmati
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Xizmatlar")
    description = models.TextField(verbose_name="Servislar xaqida")

    def __str__(self):
        return self.name


# Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Ish turi")
    image = models.ImageField(upload_to="Ishlar")

    def __str__(self):
        return self.title


#Client model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Mijozlar")
    description = models.TextField(verbose_name="Mijozlar fikri")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name