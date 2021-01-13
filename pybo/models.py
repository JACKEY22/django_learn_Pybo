from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateField()
