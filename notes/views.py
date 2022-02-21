from django.shortcuts import render, redirect


from notes.models import Note, Category

# Create your views here.

def home(request):
    hello = "Hello!!!<br>It's main page"
    return render(request, template_name='notes/home.html', context={'heloo': hello})

def notes(request):
    notes = Note.objects.all()
    return render(request, template_name='notes/notes.html', context={'notes': notes})

