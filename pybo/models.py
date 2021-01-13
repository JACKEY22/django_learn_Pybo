from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
