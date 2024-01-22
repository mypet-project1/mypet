from rest_framework import serializers

from .models import Tip


class TipSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = "__all__"

    def create(self, validated_data):
        animal = validated_data.get("animal")
        user = validated_data.get("user")
        content = validated_data.get("content")

        tip = Tip.objects.create(animal=animal, user=user, content=content)

        return tip
