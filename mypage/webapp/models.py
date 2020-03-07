from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Rating(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choices_list = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        )
    rating_value = models.CharField(max_length=20, choices=choices_list, default='0')
    count = models.IntegerField(default=0)