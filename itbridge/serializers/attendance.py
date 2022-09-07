import datetime

from rest_framework import serializers
from ..models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"

    def validate(self, attrs):
        current_date_time = datetime.datetime.now()
        current_year = current_date_time.year
        current_month = current_date_time.month
        current_day = current_date_time.day
        ten_am_date_time = datetime.datetime(year=current_year, month=current_month, day=current_day, hour=10)
        if current_date_time >= ten_am_date_time:
            raise serializers.ValidationError("You can only check in before 10 am.")
        return attrs

    def create(self, validated_data):
        check_in_today = Attendance.objects.filter(
            user=validated_data["user"], check_in=datetime.datetime.now()
        ).first()
        if not check_in_today:
            return Attendance.objects.create(
                user=validated_data["user"],
                check_in=datetime.datetime.now()
            )
        raise serializers.ValidationError("You have already checked in")
