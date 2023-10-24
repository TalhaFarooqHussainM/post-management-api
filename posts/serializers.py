from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework import serializers
from .models import Post, Image, Customer


class CustomerSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    class Meta:
        model = Customer
        fields = ('user', 'email')

    def email(self, value):
        try:
            validate_email(value)
            return True
        except ValidationError:
            return False


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('post', 'id', 'image')

    def validate_post(self, post):
        user = self.context['request'].user
        if post.customer.user != user:
            raise serializers.ValidationError("You do not have permission to perform this action.")
        return post


class PostSerializer(serializers.ModelSerializer):
    image = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'customer', 'title', 'content', 'image']
