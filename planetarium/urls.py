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

router = routers.DefaultRouter()
router.register("themes", ShowThemeView)
router.register("astronomy_shows", AstronomyShowView)
router.register("planetarium_domes", PlanetariumDomeView)
router.register("sessions", ShowSessionView)
router.register("reservations", ReservationView)
router.register("tickets", TicketView)

urlpatterns = [
    path("", include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

app_name = "planetarium"