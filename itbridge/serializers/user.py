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
    def validation_phone_number(self,phone_number):
        if phone_number.size > 4+10:
            raise serializers.ValidationError("Phonenumber must be equal ko 14 digits")
        return phone_number
