from .models import ToDos
from rest_framework import serializers

class ToDosSerializer(serializers.ModelSerializer):
  class Meta:
    model = ToDos
    fields = ('id', 'name', 'state', 'date', 'order') 