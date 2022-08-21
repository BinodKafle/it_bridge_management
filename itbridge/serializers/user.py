from rest_framework import serializers

from ..models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def validate_image(self, image):
        if image.size > 1 * 1024 * 1024:
            raise serializers.ValidationError("Image must be less than 1 MB.")
        return image

    def validate_phone_number(self, phone_number):
        if len(phone_number) > 10:
            raise serializers.ValidationError("Phone number cannot be more than 10 digits.")
        if len(phone_number) < 10:
            raise serializers.ValidationError("Phone number cannot be less than 10 digits.")
        if phone_number[:2] != "98" and phone_number[:2] != "97":
            raise serializers.ValidationError("Phone number should start with 98 or 97.")
        return phone_number
