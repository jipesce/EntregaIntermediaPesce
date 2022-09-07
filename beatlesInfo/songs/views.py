from django.shortcuts import render
from songs.models import *
from songs.forms import *
from django.template import Template, Context, loader
from django.http import HttpResponse

def inicio(request):
  return render(request, "inicio.html")


def viewSongs(request):

  if request.method == 'GET':
    searchResults = Songs.objects.all()
    mensaje = ''
    busqueda = False

  if request.method == 'POST':
    searchPattern = request.POST['pattern']
    searchResults = Songs.objects.filter(name__icontains = searchPattern)
    mensaje = f'Filtro: {searchPattern}'
    busqueda = True

  return render(request, "viewSongs.html", {'busqueda': busqueda, 'mensaje': mensaje, 'searchResults': searchResults})
  

def loadSongs(request):
  # Presenta formulario para cargar canciones.
  if request.method == 'POST':

    newSongForm = SongsForm(request.POST)
    print(newSongForm)

    if newSongForm.is_valid:
      newSongDict = newSongForm.cleaned_data
      newSong = Songs(
        name = newSongDict['name'],
        composer = newSongDict['composer'],
        album = newSongDict['album'],
        year = newSongDict['year'])

      newSong.save()
      cancionCargada = True

  else:
    newSongForm = SongsForm()
    cancionCargada = False

  return render(request, "loadSongs.html", {"cancionCargada": cancionCargada, "newSongForm": newSongForm})


def viewInstruments(request):

  if request.method == 'GET':
    print(Instruments)
    searchResults = Instruments.objects.all()
    mensaje = ''
    busqueda = False

  if request.method == 'POST':
    searchPattern = request.POST['pattern']
    searchResults = Instruments.objects.filter(type__icontains = searchPattern)
    mensaje = f'Filtro: {searchPattern}'
    busqueda = True

  return render(request, "viewInstruments.html", {'busqueda': busqueda, 'mensaje': mensaje, 'searchResults': searchResults})


def loadInstruments(request):

  if request.method == 'POST':

    newInstrumentForm = InstrumentsForm(request.POST)
    print(newInstrumentForm)

    if newInstrumentForm.is_valid:
      newInstrumentDict = newInstrumentForm.cleaned_data
      newInstrument = Instruments(
        type = newInstrumentDict['type'],
        brand = newInstrumentDict['brand'],
        model = newInstrumentDict['model'],
        year = newInstrumentDict['year'])

      newInstrument.save()
      instrumentoCargado = True

  else:
    newInstrumentForm = InstrumentsForm()
    instrumentoCargado = False

  return render(request, "loadInstruments.html", {"instrumentoCargado": instrumentoCargado, "newInstrumentForm": newInstrumentForm})


def viewMovies(request):
  movies = Movies.objects.all()

  return render(request, "viewMovies.html", {'movies': movies})

