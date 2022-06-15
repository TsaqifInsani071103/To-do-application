from django.db import models
import uuid 

# Create your models here.
class ToDos(models.Model):
  name = models.CharField(max_length = 255)
  state = models.BooleanField(default=False) 
  date = models.DateTimeField(auto_now_add=True)
  id = models.UUIDField(default = uuid.uuid4, unique=True, primary_key=True, editable=False)
  order = models.IntegerField(default = 0)
  

  def __str__(self):
    return self.name 
  
  class Meta:
    ordering = ('order', )
  
