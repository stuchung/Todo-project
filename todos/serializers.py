from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    """Django TodoSerializer"""

    class Meta:
        model = Todo
        fields = ('id', 'title_name','body', 'pub_date')
