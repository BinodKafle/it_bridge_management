from rest_framework import serializers

from ..models import holiday


class HolidaySerializer(serializers.ModelSerializer):
    class Meta:
        model = holiday
        fields = "__all__"
