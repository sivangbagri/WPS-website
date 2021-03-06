# Generated by Django 3.0.8 on 2020-07-07 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200706_1832'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(default='media/events/event.jpg', upload_to='media/events/')),
                ('image2', models.ImageField(default='media/events/event.jpg', upload_to='media/events/')),
                ('about', models.TextField()),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='notice',
            name='image',
            field=models.ImageField(default='media/notice/notice.jpg', upload_to='media/notice/'),
        ),
    ]
