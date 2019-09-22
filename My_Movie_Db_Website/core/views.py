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

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs) 
        if self.request.user.is_authenticated:
            vote = Vote.objects.get_vote_or_unsaved_blank_vote(
                movie = self.object,
                user = self.request.user
            )
        
            if vote.id:
                vote_form_url = reverse(
                    'core:UpdateVote',
                    kwargs = {
                        'movie_id' : vote.movie.id,
                        'pk': vote.id
                    }
                )
            else:
                vote_form_url = reverse(
                    'core:CreateVote',
                    kwargs = {
                        'movie_id':self.object.id
                    }
                )

            vote_form = VoteForm(instance=Vote)
            ctx['vote_form']=vote_form
            ctx['vote_form_url'] = vote_form_url
        
        return ctx

class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()

