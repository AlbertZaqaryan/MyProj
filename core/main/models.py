from django.db import models

# Create your models here.


class Contact(models.Model):

    name = models.CharField('Contact name', max_length=60)
    email = models.EmailField('Contact email')
    message = models.TextField('Contact message')

    def __str__(self):
        return f'{self.name} - {self.email}'