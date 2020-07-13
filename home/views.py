from django.shortcuts import render, HttpResponse

from .models import Contact, Teachers, Notice, Events
from django.contrib import messages


# Create your views here.
def home(request):
    messages.warning(request, '''This is not an official site of any school. Consider it as a student's project''')
    eves = Events.objects.all().order_by('-timeStamp')[:3]
    return render(request, 'home/home.html', {'eves': eves})


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        role = request.POST['role']
        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 5:
            messages.error(request, "PLease fill the form correctly! ")
        else:
            messages.success(request, "Form submitted successfully!")

        contacts = Contact(name=name, email=email, phone=phone, content=content, role=role)
        contacts.save()
    return render(request, 'home/contact.html')


def about(request):
    return render(request, 'home/about.html')


def myself(request):
    return render(request, 'home/myself.html')


def fees(request):
    return render(request, 'home/fee.html')


def teachers(request):
    teach = Teachers.objects.all()
    context = {'teach': teach}
    return render(request, 'home/teachers.html', context)


def search(request):
    query = request.GET['query']
    if len(query) > 30:
        allPosts = Notice.objects.none()

    else:
        NoticeTitle = Notice.objects.filter(title__icontains=query)
        NoticeContent = Notice.objects.filter(content__icontains=query)
        # EventTitle = Events.objects.filter(title__icontains=query)
        # EventAbout = Events.objects.filter(about__icontains=query)
        allPosts = NoticeTitle.union(NoticeContent)
    if allPosts.count() == 0:
        messages.warning(request, "No search results found. Please refine your search.")
    else:
        messages.success(request, 'Search result found.')
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)


def events(request):
    event = Events.objects.all().order_by('-timeStamp')

    return render(request, 'home/events.html', {'event': event})


def notice(request):
    notices = Notice.objects.all().order_by('-timeStamp')
    return render(request, 'home/notice.html', {'notices': notices})


def subject(request):
    if request.method == 'POST':
        subjects = request.POST.get('sub', '')
        try:
            subjects = Teachers.objects.filter(subject=subjects)
        except:
            pass
    else:
        return HttpResponse('<p><center>This content is not available in your country.</center></p>')
    return render(request, 'home/subject.html', {'subjects': subjects})
