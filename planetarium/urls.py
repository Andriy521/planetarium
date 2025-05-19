from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from planetarium.views import (
    ShowThemeView,
    AstronomyShowView,
    PlanetariumDomeView,
    ShowSessionView,
    ReservationView,
    TicketView
)

app_name = "planetarium"

router = routers.DefaultRouter()
router.register("themes", ShowThemeView, basename="showtheme")
router.register("astronomy_shows", AstronomyShowView, basename="astronomyshow")
router.register("planetarium_domes", PlanetariumDomeView, basename="planetariumdome")
router.register("sessions", ShowSessionView, basename="showsession")
router.register("reservations", ReservationView, basename="reservation")
router.register("tickets", TicketView, basename="ticket")

urlpatterns = [
    path("", include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
