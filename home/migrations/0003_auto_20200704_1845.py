# Generated by Django 3.0.8 on 2020-07-04 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachers',
            name='image',
            field=models.ImageField(default='photo.png', upload_to=''),
        ),
    ]
