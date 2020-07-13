from django.db import models


# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.TextField(max_length=100)
    role = models.CharField(max_length=30)
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.TextField()

    def __str__(self):
        return 'Message from ' + self.name


class Teachers(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    Class = models.IntegerField()
    age = models.IntegerField()
    experience = models.IntegerField()
    image = models.ImageField(upload_to='media/', default='media/photo.png')
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Notice(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/notice/', default='media/notice/notice.jpg')
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'New notice on: ' + self.title


class Events(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/events/', default='media/events/event.jpg')
    image2 = models.ImageField(upload_to='media/events/', default='media/events/event2.jpg')
    about = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'New event :' + self.title
