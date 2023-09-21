

from rest_framework import serializers

from .models import Recipe,Profile


class recipieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = '__all__'

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
