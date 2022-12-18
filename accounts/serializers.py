from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import *

User = get_user_model()


class ProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "password")


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = "__all__"


class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = "__all__"


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "__all__"


class ElementsSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ElementsSlider
        fields = "__all__"


class WorkProgramsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkPrograms
        fields = "__all__"


class MainInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainInfo
        fields = "__all__"


class CategoriesForPagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriesForPages
        fields = "__all__"


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pages
        fields = "__all__"


class MaterialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = "__all__"

class CategoriesAndPagesSerializer(serializers.ModelSerializer):
    pages = PagesSerializer(source='pages_set', many=True)
    class Meta:
        model = CategoriesForPages
        fields = "__all__"
