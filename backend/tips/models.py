import os
from django.db import models

from config import settings
from accounts.models import User
from animals.models import Animal


def tip_media_path(instance, filename):
    return f"tips/{instance.animal}/{instance.user}/{filename}"


class Tip(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="tips")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tips")
    content = models.TextField()
    tip_media = models.FileField(blank=True, upload_to=tip_media_path)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["animal"]),
            models.Index(fields=["user"]),
            models.Index(fields=["-created_at"]),
            models.Index(fields=["-updated_at"]),
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return f"[{self.animal}] {self.user}의 팁"

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT, self.tip_media.path))
        super(Tip, self).delete(*args, **kwargs)
