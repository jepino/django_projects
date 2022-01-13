# Generated by Django 3.2.5 on 2022-01-10 22:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a make (e.g. Saab)', max_length=200, validators=[django.core.validators.MaxLengthValidator(200, 'Name too long, try "Saab" instead')])),
            ],
        ),
        migrations.CreateModel(
            name='Auto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=200, validators=[django.core.validators.MaxLengthValidator(200, 'Nickname too long, try "9-3 Viggen" instead')])),
                ('mileage', models.PositiveIntegerField()),
                ('comments', models.CharField(max_length=300)),
                ('make', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='autos.make')),
            ],
        ),
    ]
