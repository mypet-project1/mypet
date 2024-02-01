from rest_framework import serializers

from .models import Hospital, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = "__all__"


class HospitalSerializer(serializers.ModelSerializer):
    review = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Hospital
        fields = [
            "name",
            "address",
            "road_address",
            "call",
            "info",
            "updated_at",
            "review",
        ]
