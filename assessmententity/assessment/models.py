from djongo import models

# Create your models here.

class QuestionObj(models.Model):
    slug = models.CharField(max_length=265, null=False)
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

class Student(models.Model):
    user_id = models.CharField(max_length=265, null=False)
    ts = models.DateTimeField(null=True)
    class Meta:
        abstract = True

class Assessment(models.Model):
    _id = models.ObjectIdField()
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

    registered_std = models.ArrayField(
        model_container=Student
    )
    attemped_std = models.ArrayField(
        model_container=Student
    )

    created_by = models.CharField(max_length=265, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class AnswerObj(models.Model):
    qn_slug = models.CharField(max_length=265, null=False)
    ans = models.TextField()
    marks = models.DecimalField()

    class Meta:
        abstract = True

class Answer(models.Model):
    _id = models.ObjectIdField()
    assessment_id = models.CharField(max_length=265, null=False)
    user_id = models.CharField(max_length=265, null=False)
    anslist = models.ArrayField(
        model_container=AnswerObj
    )
    
