from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import *

User = get_user_model()


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "password")


class PlatoonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platoon
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = "__all__"


class ElementsSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementsSlider
        fields = "__all__"


class CategoriesForPagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesForPage
        fields = "__all__"


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"


class MaterialsDistanceEducationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialsDistanceEducation
        fields = "__all__"


class PlatoonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platoon
        fields = "__all__"


class CategoriesAndPagesSerializer(serializers.ModelSerializer):
    pages = PagesSerializer(source='pages_set', many=True)

    class Meta:
        model = CategoriesForPage
        fields = "__all__"
