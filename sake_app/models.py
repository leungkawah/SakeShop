from django.db import models

class Sake(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='sake_images/', null=True, blank=True)

    def __str__(self):
        return self.name
