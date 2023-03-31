from django.views.generic import *
from djangogp.models import *
from django.urls import reverse_lazy

__all__ = [
    "RiderListView",
    "RiderDetailView",
    "RiderUpdateView",
    "RiderCreateView",
    "RiderDeleteView",
    "RaceRedirectView",
    "RaceDetailView",
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


class RaceRedirectView(RedirectView):
    def get_redirect_url(self):
        return reverse_lazy(
            "djangogp:race_detail", kwargs={"pk": Race.objects.order_by("-date")[0].pk}
        )


class RaceDetailView(DetailView):
    model = Race

    def get_context_data(self, **kwargs):
        context = {
            "race": kwargs["object"],
            "races": Race.objects.order_by("-date"),
            "results": Result.objects.all().filter(race=kwargs["object"].pk),
        }
        return context


class StandingsListView(ListView):
    model = Standings
