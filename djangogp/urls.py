from django.urls import path

from djangogp.views import (
    RiderListView,
    RaceListView,
    ResultListView,
    StandingsListView,
)

app_name = "djangogp"

urlpatterns = [
    path("riders/", RiderListView.as_view(), name="rider_list"),
    path("races/", RaceListView.as_view(), name="race_list"),
    path("standings/", StandingsListView.as_view(), name="standings_list"),
]
