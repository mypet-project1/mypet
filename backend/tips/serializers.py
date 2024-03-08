from rest_framework import serializers

from animals.serializers import AnimalSerializer
from .models import Tip


class TipSerializers(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)

    class Meta:
        model = Tip
        fields = [
            "id",
            "animal",
            "user",
            "content",
            "tip_media",
            "created_at",
            "updated_at",
        ]

    def create(self, validated_data):
        animal = validated_data.get("animal")
        user = validated_data.get("user")
        content = validated_data.get("content")
        tip_media = validated_data.get("tip_media")

        tip = Tip.objects.create(
            animal=animal, user=user, content=content, tip_media=tip_media
        )

        return tip
