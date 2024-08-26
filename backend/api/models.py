from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# write the python version here, django's ORM will automatically convert into format necessary to push into db
# the interview table in the database
class Interview(models.Model):
    title = models.CharField(max_length=100)
    role = models.TextField()
    questions = models.JSONField(blank=True, default=list)
    answers = models.JSONField(blank=True, default=list)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="interview")

    def __str__(self):
        return self.id + " for " + self.role