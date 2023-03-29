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
            role = Profile.objects.get(id=request.user.id).role
            return Response({"results": self.roles[role]}, status=200)


class ProfilesListApiView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilesSerializer
    permission_classes = (partial(IsAdmin, ['GET', 'HEAD']),)


class ProfilesByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilesSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class PlatoonsListApiView(generics.ListCreateAPIView):
    queryset = Platoon.objects.all()
    serializer_class = PlatoonsSerializer
    permission_classes = (IsAuthenticated,)


class PlatoonsByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Platoon.objects.all()
    serializer_class = PlatoonsSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class NewsListApiView(generics.ListCreateAPIView):
    queryset = New.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)


class NewsListLimitAPIView(generics.ListAPIView):
    serializer_class = NewsSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = New.objects.all()
        queryset = queryset.all()[:int(self.request.query_params.get('limit'))]
        return queryset


class NewsCreateApiView(generics.CreateAPIView):
    serializer_class = NewsSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        request.data['profile'] = request.user.id
        return super(NewsCreateApiView, self).create(request, *args, **kwargs)


class NewsByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = New.objects.all()
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


class CategoriesForPagesListApiView(generics.ListCreateAPIView):
    queryset = CategoriesForPage.objects.all()
    serializer_class = CategoriesForPagesSerializer
    permission_classes = (IsEmployee,)


class CategoriesForPagesByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriesForPage.objects.all()
    serializer_class = CategoriesForPagesSerializer
    permission_classes = (IsAuthenticated,)


class PagesListApiView(generics.ListCreateAPIView):
    queryset = Page.objects.all()
    serializer_class = PagesSerializer
    permission_classes = (IsEmployee,)

    def create(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        request.data['profile'] = request.user.id
        return super(PagesListApiView, self).create(request, *args, **kwargs)


class CategoriesAndPagesListApiView(generics.ListCreateAPIView):
    queryset = CategoriesForPage.objects.select_related()
    serializer_class = CategoriesAndPagesSerializer
    permission_classes = (IsAuthenticated,)


class PagesByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Page.objects.all()
    serializer_class = PagesSerializer
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        request.data['profile'] = request.user.id
        return self.update(request, *args, **kwargs)


class MaterialsDistanceEducationsListApiView(generics.ListCreateAPIView):
    queryset = MaterialsDistanceEducation.objects.all()
    serializer_class = MaterialsDistanceEducationsSerializer
    permission_classes = (IsAuthenticated,)


class MaterialsDistanceEducationsCreateApiView(generics.CreateAPIView):
    serializer_class = MaterialsDistanceEducationsSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        request.data['profile'] = request.user.id
        return super(MaterialsDistanceEducationsCreateApiView, self).create(request, *args, **kwargs)


class MaterialsByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MaterialsDistanceEducation.objects.all()
    serializer_class = MaterialsDistanceEducationsSerializer
    permission_classes = (AllowAny,)

    def put(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        request.data['profile'] = request.user.id
        return self.update(request, *args, **kwargs)
