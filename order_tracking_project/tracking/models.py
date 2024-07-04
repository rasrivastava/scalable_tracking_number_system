from django.db import models
import uuid

class TrackedOrder(models.Model):
    order = models.CharField(max_length=100)
    tracking_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.order} - Tracking {self.tracking_number}"
