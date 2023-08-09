from rest_framework import serializers
class TodolistSerializers(serializers.ModelSerializer):
    task_name = serializers.CharField()
    created = serializers.CharField()
    done = serializers.CharField()