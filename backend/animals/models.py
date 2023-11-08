from django.db import models

# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=25, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=["-created_at"]),
            models.Index(fields=["name"]),
        ]
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
