from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView,
                                            TokenVerifyView)

from .views import *

urlpatterns = [
    path('token/create/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('token/verify/', TokenVerifyView.as_view()),
    path('profile/', ProfilesListApiView.as_view()),
    path('profile/create/', ProfilesCreateAPIView.as_view()),
    path('profile/<int:id>', ProfilesByIdAPIView.as_view()),
    path('position/', PositionsListApiView.as_view()),
    path('position/create/', PositionsCreateAPIView.as_view()),
    path('position/<int:id>', PositionsByIdAPIView.as_view()),
    path('phone/', PhonesListApiView.as_view()),
    path('phone/create/', PhonesCreateApiView.as_view()),
    path('phone/<int:id>', PhonesByIdApiView.as_view()),
    path('news/', NewsListApiView.as_view()),
    path('news/create/', NewsCreateApiView.as_view()),
    path('news/<int:id>', NewsByIdApiView.as_view()),
    path('elements-slider/', ElementsSliderListApiView.as_view()),
    path('elements-slider/create/', ElementsSliderCreateApiView.as_view()),
    path('elements-slider/<int:id>', ElementsSliderByIdApiView.as_view()),
    path('work-programs/', WorkProgramsListApiView.as_view()),
    path('work-programs/create/', WorkProgramsDownloadApiView.as_view()),
    path('work-programs/<int:id>', WorkProgramsByIdApiView.as_view()),
    path('main-info/', MainInfoListApiView.as_view()),
    path('main-info/create/', MainInfoCreateApiView.as_view()),
    path('main-info/<int:id>', MainInfoByIdApiView.as_view()),
    path('category-for-page/', CategoriesForPagesListApiView.as_view()),
    path('category-for-page/create/', CategoriesForPagesCreateApiView.as_view()),
    path('category-for-page/<int:id>', CategoriesForPagesByIdApiView.as_view()),
    path('page/', PagesListApiView.as_view()),
    path('page/create/', PagesCreateApiView.as_view()),
    path('page/<int:id>', PagesByIdApiView.as_view()),
]
