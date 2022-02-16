from django.shortcuts import render, redirect


from notes.models import Note, Category

# Create your views here.

def home(request):
    notes = Note.objects.all()
    return render(request, template_name='notes/home.html', context={'notes': notes})

def notes(request):
    notes = Note.objects.all()
    pass

