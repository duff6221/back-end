from rest_framework import serializers


class JobPostingSerializer(serializers.Serializer):
    job_posting = serializers.CharField(
        required=True,
        allow_blank=False
    )
