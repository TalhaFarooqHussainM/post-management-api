from rest_framework import serializers
from .models import Post, Image, Customer
from django.contrib.auth.models import User

class CustomerSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    email = serializers.EmailField()

    class Meta:
        model = Customer
        fields = ('user', 'email')

    def validate_email(self, value):
        if not value.endswith('@gmail.com'):
            raise serializers.ValidationError('Email must end with @gmail.com')
        return value
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
    # customer = serializers.ReadOnlyField(source='customer.username')
    image = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'customer', 'title', 'content', 'image']
