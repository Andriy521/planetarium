from rest_framework import serializers
from django.db import IntegrityError

from planetarium.models import (
    ShowTheme,
    AstronomyShow,
    PlanetariumDome,
    ShowSession,
    Reservation,
    Ticket,
)


class ShowThemeSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = ShowTheme
        fields = "__all__"


class AstronomyShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = AstronomyShow
        fields = "__all__"


class PlanetariumDomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetariumDome
        fields = "__all__"


class ShowSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowSession
        fields = "__all__"


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = "__all__"


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = "__all__"

    def validate(self, data):
        row = data("row")
        seat = data("seat")
        show_session = data("show_session")

        if Ticket.objects.filter(row=row, seat=seat, show_session=show_session).exists():
            raise serializers.ValidationError("Ticket already taken")

        dome = show_session.planetarium_dome
        if row < 1 or row > dome.rows:
            raise serializers.ValidationError(
                f"Row number must be between 1 and {dome.rows}."
            )
        if seat < 1 or seat > dome.seats_in_row:
            raise serializers.ValidationError(
                f"Seat number must be between 1 and {dome.seats_in_row}."
            )

        return data

