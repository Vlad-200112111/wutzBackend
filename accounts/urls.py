from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView,
                                            TokenBlacklistView)

from .views import *

urlpatterns = [
    path('token/create/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('logout/', TokenBlacklistView.as_view()),
    path('profile/', ProfilesListApiView.as_view()),
    path('profile/<int:pk>', ProfilesByIdAPIView.as_view()),
    path('position/', PositionsListApiView.as_view()),
    path('position/<int:pk>', PositionsByIdAPIView.as_view()),
    path('phone/', PhonesListApiView.as_view()),
    path('phone/<int:pk>', PhonesByIdApiView.as_view()),
    path('news/', NewsListApiView.as_view()),
    path('news/create/', NewsCreateApiView.as_view()),
    path('news/limit/', NewsListLimitAPIView.as_view()),
    path('news/<int:pk>', NewsByIdApiView.as_view()),
    path('elements-slider/', ElementsSliderListApiView.as_view()),
    path('elements-slider/<int:pk>', ElementsSliderByIdApiView.as_view()),
    path('work-programs/', WorkProgramsListApiView.as_view()),
    path('work-programs/<int:pk>', WorkProgramsByIdApiView.as_view()),
    path('main-info/', MainInfoListApiView.as_view()),
    path('main-info/<int:pk>', MainInfoByIdApiView.as_view()),
    path('category-for-page/', CategoriesForPagesListApiView.as_view()),
    path('category-for-page/<int:pk>', CategoriesForPagesByIdApiView.as_view()),
    path('page/', PagesListApiView.as_view()),
    path('page/create/', PagesCreateApiView.as_view()),
    path('page/<int:pk>', PagesByIdApiView.as_view()),
    path('categories-and-pages/', CategoriesAndPagesListApiView.as_view()),
]
