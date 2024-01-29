from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from accounts.models import User


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    call = models.CharField(max_length=20)
    info = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["name"]),
            models.Index(fields=["call"]),
            models.Index(fields=["-created_at"]),
            models.Index(fields=["-updated_at"]),
        ]
        ordering = ["name"]

    def str(self):
        return f"{self.name} - {self.call}"


class Review(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hospital_review"
    )
    hospital = models.ForeignKey(
        Hospital, on_delete=models.CASCADE, related_name="review"
    )
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    grade = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=["user"]),
            models.Index(fields=["hospital"]),
            models.Index(fields=["grade"]),
            models.Index(fields=["-created_at"]),
            models.Index(fields=["-updated_at"]),
        ]
        ordering = ["-created_at"]

    def str(self):
        return f"[{self.hospital}] {self.user} review"
