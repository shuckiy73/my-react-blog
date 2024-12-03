from rest_framework import serializers
from .models import Post

# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'  # or specify individual fields if needed


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'