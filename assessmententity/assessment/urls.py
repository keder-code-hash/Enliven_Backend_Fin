from django.urls import path
from views import *

urlpatterns = [
    path('', AssessmentList.as_view(), name='assessments'),
]
