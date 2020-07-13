# Generated by Django 3.0.8 on 2020-07-04 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('Class', models.IntegerField()),
                ('age', models.IntegerField()),
                ('experience', models.IntegerField()),
                ('image', models.ImageField(default='static/photo.png', upload_to='')),
                ('subject', models.CharField(max_length=100)),
            ],
        ),
    ]
