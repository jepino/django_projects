from django.db import models
from django.core.validators import MaxLengthValidator


class Make(models.Model):
    name = models.CharField(
        max_length=200,
        help_text='Enter a make (e.g. Saab)',
        validators=[MaxLengthValidator(200, 'Name too long, try "Saab" instead')]
    )

    def __str__(self):
        return self.name

class Auto(models.Model):
    nickname = models.CharField(
        max_length=200,
        validators=[MaxLengthValidator(200, 'Nickname too long, try "9-3 Viggen" instead')]
    )
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=True)
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)

    def __str__(self):
        return self.nickname