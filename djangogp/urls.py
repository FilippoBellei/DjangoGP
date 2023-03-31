from django.urls import path
from djangogp.views import *

app_name = "djangogp"

urlpatterns = [
    path("riders/", RiderListView.as_view(), name="rider_list"),
    path("rider/<int:pk>/", RiderDetailView.as_view(), name="rider_detail"),
    path("rider/<int:pk>/update/", RiderUpdateView.as_view(), name="rider_update"),
    path("rider/create/", RiderCreateView.as_view(), name="rider_create"),
    path("rider/<int:pk>/delete/", RiderDeleteView.as_view(), name="rider_delete"),
    path("races", RaceRedirectView.as_view(), name="race_list"),
    path("race/<int:pk>/", RaceDetailView.as_view(), name="race_detail"),
    path("", StandingsListView.as_view(), name="standings_list"),
]
