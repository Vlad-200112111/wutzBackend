from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Profiles, Positions, Phones, News, MainInfo, CategoriesForPages, Pages, ElementsSlider, WorkPrograms
from .serializers import ProfilesSerializer, PositionsSerializer, PhonesSerializer, NewsSerializer, PagesSerializer, \
    ElementsSliderSerializer, WorkProgramsSerializer, MainInfoSerializer, CategoriesForPagesSerializer


class ProfilesListApiView(generics.ListAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class ProfilesCreateAPIView(generics.CreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class ProfilesByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class PositionsListApiView(generics.ListAPIView):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class PositionsCreateAPIView(generics.CreateAPIView):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class PositionsByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class PhonesListApiView(generics.ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class PhonesCreateApiView(generics.CreateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class PhonesByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class NewsListApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class NewsCreateApiView(generics.CreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class NewsByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class ElementsSliderListApiView(generics.ListAPIView):
    queryset = ElementsSlider.objects.all()
    serializer_class = ElementsSliderSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class ElementsSliderCreateApiView(generics.CreateAPIView):
    queryset = ElementsSlider.objects.all()
    serializer_class = ElementsSliderSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class ElementsSliderByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElementsSlider.objects.all()
    serializer_class = ElementsSliderSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class WorkProgramsListApiView(generics.ListAPIView):
    queryset = WorkPrograms.objects.all()
    serializer_class = WorkProgramsSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class WorkProgramsDownloadApiView(generics.CreateAPIView):
    queryset = WorkPrograms.objects.all()
    serializer_class = WorkProgramsSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class WorkProgramsByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkPrograms.objects.all()
    serializer_class = WorkProgramsSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class MainInfoListApiView(generics.ListAPIView):
    queryset = MainInfo.objects.all()
    serializer_class = MainInfoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class MainInfoCreateApiView(generics.CreateAPIView):
    queryset = MainInfo.objects.all()
    serializer_class = MainInfoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class MainInfoByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainInfo.objects.all()
    serializer_class = MainInfoSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class CategoriesForPagesListApiView(generics.ListAPIView):
    queryset = CategoriesForPages.objects.all()
    serializer_class = CategoriesForPagesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class CategoriesForPagesCreateApiView(generics.CreateAPIView):
    queryset = CategoriesForPages.objects.all()
    serializer_class = CategoriesForPagesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class CategoriesForPagesByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriesForPages.objects.all()
    serializer_class = CategoriesForPagesSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class PagesListApiView(generics.ListAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class PagesCreateApiView(generics.CreateAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]


class PagesByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)
    authentication_classes = [JWTAuthentication]
