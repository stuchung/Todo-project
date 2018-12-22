from django.db import models
import datetime
# Create your models here.

class Todo(models.Model):
    """Django data model Todo"""
    title_name = models.CharField(blank=True, max_length=100)
    body = models.TextField(blank=True)
    pub_date = models.DateField(default=datetime.datetime.today)

    class Meta:
        verbose_name = 'Todo'
        verbose_name_plural = 'Todos'

    def __str__(self):
        return str(self.title_name)
