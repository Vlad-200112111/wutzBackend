from functools import partial
from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .permissions import *


class GetRole(generics.GenericAPIView):
    roles = {1: 'ADMIN', 2: 'STUDENT', 3: 'TEACHER', 4: 'EMPLOYEE'}
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"results": "Unauthorized"}, status=401)
        else:
            role = Profiles.objects.get(id=request.user.id).role
            return Response({"results": self.roles[role]}, status=200)


class ProfilesListApiView(generics.ListCreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    permission_classes = (partial(IsAdmin, ['GET', 'HEAD']),)


class ProfilesByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class PositionsListApiView(generics.ListCreateAPIView):
    queryset = Platoons.objects.all()
    serializer_class = PlatoonsSerializer
    permission_classes = (IsAuthenticated,)


class PositionsByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platoons.objects.all()
    serializer_class = PlatoonsSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class PhonesListApiView(generics.ListCreateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = (IsAuthenticated,)


class PhonesByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class NewsListApiView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)


class NewsListLimitAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = News.objects.all()
        queryset = queryset.all()[:int(self.request.query_params.get('limit'))]
        return queryset


class NewsCreateApiView(generics.CreateAPIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        request.data['profile'] = request.user.id
        return super(NewsCreateApiView, self).create(request, *args, **kwargs)


class NewsByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)


class ElementsSliderListApiView(generics.ListCreateAPIView):
    queryset = ElementsSlider.objects.all()
    serializer_class = ElementsSliderSerializer
    permission_classes = (IsAuthenticated,)


class ElementsSliderByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElementsSlider.objects.all()
    serializer_class = ElementsSliderSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class WorkProgramsListApiView(generics.ListCreateAPIView):
    queryset = WorkPrograms.objects.all()
    serializer_class = WorkProgramsSerializer
    permission_classes = (IsAuthenticated,)


class WorkProgramsByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkPrograms.objects.all()
    serializer_class = WorkProgramsSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class MainInfoListApiView(generics.ListCreateAPIView):
    queryset = MainInfo.objects.all()
    serializer_class = MainInfoSerializer
    permission_classes = (IsAuthenticated,)


class MainInfoByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MainInfo.objects.all()
    serializer_class = MainInfoSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        request.data['profile'] = request.user.id
        return self.update(request, *args, **kwargs)


class CategoriesForPagesListApiView(generics.ListCreateAPIView):
    queryset = CategoriesForPages.objects.all()
    serializer_class = CategoriesForPagesSerializer
    permission_classes = (IsAuthenticated,)


class CategoriesForPagesByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriesForPages.objects.all()
    serializer_class = CategoriesForPagesSerializer
    permission_classes = (IsAuthenticated,)


class PagesListApiView(generics.ListCreateAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    permission_classes = (IsAuthenticated,)


class CategoriesAndPagesListApiView(generics.ListCreateAPIView):
    queryset = CategoriesForPages.objects.select_related()
    serializer_class = CategoriesAndPagesSerializer
    permission_classes = (IsAuthenticated,)


class PagesCreateApiView(generics.CreateAPIView):
    serializer_class = PagesSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        request.data['profile'] = request.user.id
        return super(PagesCreateApiView, self).create(request, *args, **kwargs)


class PagesByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        request.data['profile'] = request.user.id
        return self.update(request, *args, **kwargs)


class MaterialsListApiView(generics.ListCreateAPIView):
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    permission_classes = (IsAuthenticated,)


class MaterialsCreateApiView(generics.CreateAPIView):
    serializer_class = MaterialsSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        request.data['profile'] = request.user.id
        return super(MaterialsCreateApiView, self).create(request, *args, **kwargs)


class MaterialsByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Materials.objects.all()
    serializer_class = MaterialsSerializer
    permission_classes = (AllowAny,)

    def put(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        request.data['profile'] = request.user.id
        return self.update(request, *args, **kwargs)
