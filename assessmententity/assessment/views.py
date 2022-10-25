from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from assessment.models import Assessment
from assessment.serializers.AssessmentModel import AssessmentSerializer

# Create your views here.

class AssessmentList(APIView):
    def get(self, request):
        t = request.data["type"]
        if t == "upcoming":
            pass
        elif t == "ongoing":
            queryset = Assessment.objects.filter(ongoing=True)
            serializer = AssessmentSerializer(queryset)
            Response(serializer.data)
        elif t == "registered":
            pass
        else:
            pass

