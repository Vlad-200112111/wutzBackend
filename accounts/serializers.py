from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Phones, News, ElementsSlider, WorkPrograms, MainInfo, CategoriesForPages, Pages, Positions

User = get_user_model()


class ProfilesSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ("id", "email", "username", "first_name", "last_name", "password")


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Positions
        fields = "__all__"


class PhonesSerializer(serializers.Serializer):
    class Meta:
        model = Phones
        fields = "__all__"


class NewsSerializer(serializers.Serializer):
    class Meta:
        model = News
        fields = "__all__"


class ElementsSliderSerializer(serializers.Serializer):
    class Meta:
        model = ElementsSlider
        fields = "__all__"


class WorkProgramsSerializer(serializers.Serializer):
    class Meta:
        model = WorkPrograms
        fields = "__all__"


class MainInfoSerializer(serializers.Serializer):
    class Meta:
        model = MainInfo
        fields = "__all__"


class CategoriesForPagesSerializer(serializers.Serializer):
    class Meta:
        model = CategoriesForPages
        fields = "__all__"


class PagesSerializer(serializers.Serializer):
    class Meta:
        model = Pages
        fields = "__all__"
