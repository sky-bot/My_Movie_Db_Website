from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Movie, Person
# Create your views here.

class MovieList(ListView):
    model = Movie
    paginate_by = 10

class MovieDetail(DetailView):
    queryset = (
        Movie.objects.all_with_related_person()
    )

class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()

