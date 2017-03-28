from rest_framework import serializers

class UrlSerializer(serializers.Serializer):
    url = serializers.CharField(max_length=None, min_length=None, allow_blank=False, trim_whitespace=True)