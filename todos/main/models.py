from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=280)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    done = models.BooleanField()

