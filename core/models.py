from django.db import models

# Create your models here.
class Message(models.Model):
  name = models.CharField(max_length=300)
  email = models.CharField(max_length=300)
  message = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.name