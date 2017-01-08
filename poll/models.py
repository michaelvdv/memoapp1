from django.db import models
from django.utils import timezone


# Create your models here.
class Question(models.Model):
    author = models.CharField(max_length=1000)
    question_text=models.CharField(max_length=1000)
    pub_date=models.DateTimeField(default=timezone.now)
    likes = models.PositiveIntegerField(default=0)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
