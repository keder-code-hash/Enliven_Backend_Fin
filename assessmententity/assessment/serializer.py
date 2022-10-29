from rest_framework import serializers

class AssessmentSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=265)
    desc = serializers.CharField(max_length=1024)
    sub = serializers.CharField(max_length=128)
    noq = serializers.IntegerField(default=0)
    fmarks = serializers.IntegerField(default=0)
    duration = serializers.TimeField()
    ongoing = serializers.BooleanField()
    start_date = serializers.DateTimeField()
    end_date = serializers.DateTimeField()
