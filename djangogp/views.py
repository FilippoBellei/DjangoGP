from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Rider, Race, Result, Standings

__all__ = [
    "RiderListView",
    "RaceListView",
    "ResultListView",
    "StandingsListView",
]


class RiderListView(ListView):
    model = Rider


class RaceListView(ListView):
    model = Race


class ResultListView(ListView):
    model = Result


class StandingsListView(ListView):
    model = Standings
