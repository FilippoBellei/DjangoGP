from django.urls import path

from djangogp.views import (
    RiderListView,
    RaceListView,
    ResultListView,
    StandingsListView,
)

app_name = "djangogp"

urlpatterns = [
    path("riders/", RiderListView.as_view()),
    path("races/", RaceListView.as_view()),
    path("results/", ResultListView.as_view()),
    path("standings/", StandingsListView.as_view()),
]
