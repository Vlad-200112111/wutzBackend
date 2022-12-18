import itertools

from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import *
from .serializers import *


class ProfilesListApiView(generics.ListAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    permission_classes = (IsAuthenticated,)


class ProfilesCreateAPIView(generics.CreateAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    permission_classes = (IsAuthenticated,)


class ProfilesByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profiles.objects.all()
    serializer_class = ProfilesSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class PositionsListApiView(generics.ListAPIView):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer
    permission_classes = (IsAuthenticated,)


class PositionsCreateAPIView(generics.CreateAPIView):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer
    permission_classes = (IsAuthenticated,)


class PositionsByIdAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Positions.objects.all()
    serializer_class = PositionsSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class PhonesListApiView(generics.ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = (IsAuthenticated,)


class PhonesCreateApiView(generics.CreateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    permission_classes = (IsAuthenticated,)


class PhonesByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhonesSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class NewsListApiView(generics.ListAPIView):
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


class ElementsSliderListApiView(generics.ListAPIView):
    queryset = ElementsSlider.objects.all()
    serializer_class = ElementsSliderSerializer
    permission_classes = (IsAuthenticated,)


class ElementsSliderCreateApiView(generics.CreateAPIView):
    queryset = ElementsSlider.objects.all()
    serializer_class = ElementsSliderSerializer
    permission_classes = (IsAuthenticated,)


class ElementsSliderByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ElementsSlider.objects.all()
    serializer_class = ElementsSliderSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class WorkProgramsListApiView(generics.ListAPIView):
    queryset = WorkPrograms.objects.all()
    serializer_class = WorkProgramsSerializer
    permission_classes = (IsAuthenticated,)


class WorkProgramsDownloadApiView(generics.CreateAPIView):
    queryset = WorkPrograms.objects.all()
    serializer_class = WorkProgramsSerializer
    permission_classes = (IsAuthenticated,)


class WorkProgramsByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkPrograms.objects.all()
    serializer_class = WorkProgramsSerializer
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)


class MainInfoListApiView(generics.ListAPIView):
    queryset = MainInfo.objects.all()
    serializer_class = MainInfoSerializer
    permission_classes = (IsAuthenticated,)


class MainInfoCreateApiView(generics.CreateAPIView):
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


class CategoriesForPagesListApiView(generics.ListAPIView):
    queryset = CategoriesForPages.objects.all()
    serializer_class = CategoriesForPagesSerializer
    permission_classes = (IsAuthenticated,)


class CategoriesForPagesCreateApiView(generics.CreateAPIView):
    queryset = CategoriesForPages.objects.all()
    serializer_class = CategoriesForPagesSerializer
    permission_classes = (IsAuthenticated,)


class CategoriesForPagesByIdApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CategoriesForPages.objects.all()
    serializer_class = CategoriesForPagesSerializer
    permission_classes = (IsAuthenticated,)


class PagesListApiView(generics.ListAPIView):
    queryset = Pages.objects.all()
    serializer_class = PagesSerializer
    permission_classes = (IsAuthenticated,)

class CategoriesAndPagesListApiView(generics.ListAPIView):
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


class MaterialsListApiView(generics.ListAPIView):
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
    permission_classes = (IsAuthenticated,)

    def put(self, request, *args, **kwargs):
        self.request.POST._mutable = True
        request.data['profile'] = request.user.id
        return self.update(request, *args, **kwargs)
