from django.db import models
from event.models import Event,Chair 
from django.contrib.auth.models import User

# Create your models here.
class Reservation(models.Model):
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_event = models.ForeignKey(Event, on_delete=models.CASCADE)
    chair = models.ForeignKey(Chair, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, editable=False)
    class Meta:
        unique_together = ('chair', 'id_event') 

    def __str__(self):
        return f"Reservation {self.id} for user {self.id_user} and event {self.id_event}"