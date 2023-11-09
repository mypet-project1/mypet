from django.db import models

from accounts.models import User
from animals.models import Animal


class Tip(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="tips")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tips")
    content = models.TextField()
    tip_media = models.FileField(blank=True, upload_to="")
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
