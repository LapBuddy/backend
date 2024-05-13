from rest_framework import serializers
from .models import Setup, Session, Post


class SetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setup
        fields = ["name", "make", "model", "year", "tires", "pressure", "suspension", "other"]

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"