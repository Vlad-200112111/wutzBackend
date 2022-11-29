from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import Profiles, Positions, Phones, News, MainInfo, CategoriesForPages, Pages, ElementsSlider, WorkPrograms
from .serializers import ProfilesSerializer, PositionsSerializer, PhonesSerializer, NewsSerializer, PagesSerializer, \
    ElementsSliderSerializer, WorkProgramsSerializer, MainInfoSerializer, CategoriesForPagesSerializer


class ProfilesListApiView(generics.ListAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    permission_classes = [IsAuthenticated]


class ProfilesCreateAPIView(generics.CreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    permission_classes = [IsAuthenticated]


class ProfilesByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class PositionsListApiView(generics.ListAPIView):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer
    permission_classes = [IsAuthenticated]


class PositionsCreateAPIView(generics.CreateAPIView):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer
    permission_classes = [IsAuthenticated]


class PositionsByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class PhonesListApiView(generics.ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = [IsAuthenticated]


class PhonesCreateApiView(generics.CreateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = [IsAuthenticated]


class PhonesByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class NewsListApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]


class NewsCreateApiView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAuthenticated]


class NewsByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class ElementsSliderListApiView(generics.ListAPIView):
    queryset = ElementsSlider.objects.all()
    serializer_class = ElementsSliderSerializer
    permission_classes = [IsAuthenticated]


class ElementsSliderCreateApiView(generics.CreateAPIView):
    queryset = ElementsSlider.objects.all()
    serializer_class = ElementsSliderSerializer
    permission_classes = [IsAuthenticated]


class ElementsSliderByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElementsSlider.objects.all()
    serializer_class = ElementsSliderSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class WorkProgramsListApiView(generics.ListAPIView):
    queryset = WorkPrograms.objects.all()
    serializer_class = WorkProgramsSerializer
    permission_classes = [IsAuthenticated]


class WorkProgramsDownloadApiView(generics.CreateAPIView):
    queryset = WorkPrograms.objects.all()
    serializer_class = WorkProgramsSerializer
    permission_classes = [IsAuthenticated]


class WorkProgramsByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkPrograms.objects.all()
    serializer_class = WorkProgramsSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class MainInfoListApiView(generics.ListAPIView):
    queryset = MainInfo.objects.all()
    serializer_class = MainInfoSerializer
    permission_classes = [IsAuthenticated]


class MainInfoCreateApiView(generics.CreateAPIView):
    queryset = MainInfo.objects.all()
    serializer_class = MainInfoSerializer
    permission_classes = [IsAuthenticated]


class MainInfoByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainInfo.objects.all()
    serializer_class = MainInfoSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class CategoriesForPagesListApiView(generics.ListAPIView):
    queryset = CategoriesForPages.objects.all()
    serializer_class = CategoriesForPagesSerializer
    permission_classes = [IsAuthenticated]


class CategoriesForPagesCreateApiView(generics.CreateAPIView):
    queryset = CategoriesForPages.objects.all()
    serializer_class = CategoriesForPagesSerializer
    permission_classes = [IsAuthenticated]


class CategoriesForPagesByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriesForPages.objects.all()
    serializer_class = CategoriesForPagesSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]


class PagesListApiView(generics.ListAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    permission_classes = [IsAuthenticated]


class PagesCreateApiView(generics.CreateAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    permission_classes = [IsAuthenticated]


class PagesByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]
