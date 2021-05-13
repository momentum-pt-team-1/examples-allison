from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=280)
    created_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True, null=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.text
