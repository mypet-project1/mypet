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
            "id",
            "name",
            "address",
            "road_address",
            "call",
            "info",
            "updated_at",
            "review",
        ]

    def create(self, validated_data):
        name = validated_data.get("name")
        address = validated_data.get("address")
        road_address = validated_data.get("road_address")
        call = validated_data.get("call")
        info = validated_data.get("info")

        hospital = Hospital.objects.create(
            name=name, address=address, road_address=road_address, call=call, info=info
        )

        return hospital
