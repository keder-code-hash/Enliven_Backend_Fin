from email.policy import default
from djongo import models

# Create your models here.

class QuestionObj(models.Model):
    qn = models.TextField()
    ans = models.TextField()
    mark = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True
        

class Question(models.Model):
    qlist = models.ArrayField(
        model_container=QuestionObj
    )

    class Meta:
        abstract = True

class Assessment(models.Model):
    title = models.CharField(max_length=265)
    desc = models.TextField()
    sub = models.CharField(max_length=128, null=False)
    questions = models.EmbeddedField(
        model_container = Question
    )
    noq = models.PositiveIntegerField(default=0)
    fmarks = models.PositiveIntegerField(default=0)
    duration = models.TimeField()
    ongoing = models.BooleanField(default=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_by = models.CharField(max_length=265, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Answer(models.Model):
    assessment_id = models.BigIntegerField()
    pass