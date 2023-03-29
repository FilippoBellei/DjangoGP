from django.views.generic import *
from django.urls import reverse_lazy
from djangogp.models import *

__all__ = [
    "RiderListView",
    "RiderDetailView",
    "RiderUpdateView",
    "RiderCreateView",
    "RiderDeleteView",
    "RaceListView",
    "ResultListView",
    "StandingsListView",
]


class RiderListView(ListView):
    model = Rider


class RiderDetailView(DetailView):
    model = Rider


class RiderUpdateView(UpdateView):
    model = Rider
    fields = (
        "name",
        "country",
        "team",
        "bike",
        "dateOfBirth",
        "placeOfBirth",
        "height",
        "weight",
    )

    def get_success_url(self):
        return reverse_lazy("djangogp:rider_detail", kwargs={"pk": self.object.id})


class RiderCreateView(CreateView):
    model = Rider
    fields = (
        "name",
        "country",
        "team",
        "bike",
        "dateOfBirth",
        "placeOfBirth",
        "height",
        "weight",
    )

    def get_success_url(self):
        return reverse_lazy("djangogp:rider_list")


class RiderDeleteView(DeleteView):
    model = Rider
    success_url = reverse_lazy("djangogp:rider_list")


class RaceListView(ListView):
    model = Race


class ResultListView(ListView):
    model = Result


class StandingsListView(ListView):
    model = Standings
