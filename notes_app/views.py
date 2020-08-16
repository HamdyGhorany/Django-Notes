from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from requests import Response
from rest_framework.response import Response
from .models import Notes , NewNote
from .forms import NoteForm
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.views import APIView
from .json import JsonNote , Json_New_Notes
from rest_framework import  viewsets
import requests


# Create your views here.


#APIs

class JsonNewNotes(viewsets.ModelViewSet):
    queryset = NewNote.objects.all()
    serializer_class = Json_New_Notes

class Json_Note(viewsets.ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = JsonNote



#APIs
class notes_list(APIView):
    def get(self, request):
        s1= Notes.objects.all()
        s2= JsonNote(s1, many=True)
        return Response(s2.data)
    def post(self):
        pass

class notes_list1(viewsets.ModelViewSet):
    pass





#show all notes
def all_notes(request):
    #return HttpResponse('<h1> Welcome In Django </h1>', {})
    all_notes = Notes.objects.all()
    context = {
        'all_notes' : all_notes
    }
    return render(request, 'notes.html', context)

#show one note
def detail(request, slug):
    note = Notes.objects.get(slug=slug)
    context = {
        'note' : note
    }
    return render(request, 'one_note.html', context)



def note_add(request):
    #form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Profile details updated.')
            return redirect('/notes')
    else:
        form = NoteForm()


    context = {
        'form' : form ,
    }
    return render(request, 'add.html', context)

def edit(request, slug):
    notes = get_object_or_404(Notes, slug=slug)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance = notes)

        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            messages.success(request, 'Profile details updated.')
            return redirect('/notes')
    else:
        form = NoteForm(instance = notes)


    context = {
        'form' : form ,
    }
    return render(request, 'create.html', context)


#get api

def get_date(request):
    url = 'http://adioon.pythonanywhere.com/json/sho/'
    date = requests.get(url).json()
    context = {
        'data' : date
    }
    return render(request, 'in.html', context)