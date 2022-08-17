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
