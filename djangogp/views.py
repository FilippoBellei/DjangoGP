from django.views.generic import *
from djangogp.models import *
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

__all__ = [
    "RiderListView",
    "RiderDetailView",
    "RiderUpdateView",
    "RiderCreateView",
    "RiderDeleteView",
    "RaceRedirectView",
    "RaceDetailView",
]


class RiderListView(ListView):
    model = Rider
    ordering = ["-points"]


class RiderDetailView(DetailView):
    model = Rider


@method_decorator(login_required, name="dispatch")
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


@method_decorator(login_required, name="dispatch")
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


@method_decorator(login_required, name="dispatch")
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
            "results": Result.objects.filter(race=kwargs["object"].pk).order_by(
                "position"
            ),
        }
        return context
