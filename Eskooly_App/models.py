from django.db import models

# Create your models here.
class Classes(models.Model):
    Name_of_class = models.CharField(max_length=200)
    Monthly_fees = models.IntegerField()
    def __str__(self):
        return self.Name_of_class
