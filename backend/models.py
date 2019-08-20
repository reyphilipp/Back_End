from django.db import models

class Address(models.Model):
    name = models.CharField(max_length=125)
    street = models.CharField(max_length=125)
    postcode = models.CharField(max_length=10)
    city = models.CharField(max_length=125)

    def __str__(self):
        return '%s, %s %s' % (self.name,
                              self.postcode,
                              self.city)