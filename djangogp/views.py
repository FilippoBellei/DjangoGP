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
    "RaceDetailView",
    "RaceUpdateView",
    "RaceCreateView",
    "RaceDeleteView",
    "ResultListView",
    "ResultDetailView",
    "ResultUpdateView",
    "ResultCreateView",
    "ResultDeleteView",
    "StandingsListView",
    "StandingsDetailView",
    "StandingsUpdateView",
    "StandingsCreateView",
    "StandingsDeleteView",
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


class RaceDetailView(DetailView):
    model = Race


class RaceUpdateView(UpdateView):
    model = Race
    fields = (
        "name",
        "city",
        "date",
        "temperature",
        "weather",
        "trackCondition",
        "humidity",
        "groundTemperature",
    )

    def get_success_url(self):
        return reverse_lazy("djangogp:race_detail", kwargs={"pk": self.object.id})


class RaceCreateView(CreateView):
    model = Race
    fields = (
        "name",
        "city",
        "date",
        "temperature",
        "weather",
        "trackCondition",
        "humidity",
        "groundTemperature",
    )

    def get_success_url(self):
        return reverse_lazy("djangogp:race_list")


class RaceDeleteView(DeleteView):
    model = Race
    success_url = reverse_lazy("djangogp:race_list")


class ResultListView(ListView):
    model = Result


class ResultDetailView(DetailView):
    model = Result


class ResultUpdateView(UpdateView):
    model = Result
    fields = (
        "position",
        "points",
        "rider",
        "race",
    )

    def get_success_url(self):
        return reverse_lazy("djangogp:result_detail", kwargs={"pk": self.object.id})


class ResultCreateView(CreateView):
    model = Result
    fields = (
        "position",
        "points",
        "rider",
        "race",
    )

    def get_success_url(self):
        return reverse_lazy("djangogp:result_list")


class ResultDeleteView(DeleteView):
    model = Result
    success_url = reverse_lazy("djangogp:result_list")


class StandingsListView(ListView):
    model = Standings


class StandingsDetailView(DetailView):
    model = Standings


class StandingsUpdateView(UpdateView):
    model = Standings
    fields = (
        "position",
        "points",
        "rider",
    )

    def get_success_url(self):
        return reverse_lazy("djangogp:standings_detail", kwargs={"pk": self.object.id})


class StandingsCreateView(CreateView):
    model = Standings
    fields = (
        "position",
        "points",
        "rider",
    )

    def get_success_url(self):
        return reverse_lazy("djangogp:standings_list")


class StandingsDeleteView(DeleteView):
    model = Standings
    success_url = reverse_lazy("djangogp:standings_list")
