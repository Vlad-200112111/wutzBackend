from django.urls import path

from .views import *

urlpatterns = [
    path('profile/', ProfilesListApiView.as_view()),
    path('profile/create/', ProfilesCreateAPIView.as_view()),
    path('profile/<int:pk>/', ProfilesByIdAPIView.as_view()),
    path('position/', PositionsListApiView.as_view()),
    path('position/create/', PositionsCreateAPIView.as_view()),
    path('position/<int:pk>/', PositionsByIdAPIView.as_view()),
    path('phone/', PhonesListApiView.as_view()),
    path('phone/create/', PhonesCreateApiView.as_view()),
    path('phone/<int:pk>/', PhonesByIdApiView.as_view()),
    path('news/', NewsListApiView.as_view()),
    path('news/create/', NewsCreateApiView.as_view()),
    path('news/<int:pk>/', NewsByIdApiView.as_view()),
    path('elements-slider/', ElementsSliderListApiView.as_view()),
    path('elements-slider/create/', ElementsSliderCreateApiView.as_view()),
    path('elements-slider/<int:pk>/', ElementsSliderByIdApiView.as_view()),
    path('work-programs/', WorkProgramsListApiView.as_view()),
    path('work-programs/create/', WorkProgramsDownloadApiView.as_view()),
    path('work-programs/<int:pk>/', WorkProgramsByIdApiView.as_view()),
    path('main-info/',MainInfoListApiView.as_view()),
    path('main-info/create/', MainInfoCreateApiView.as_view()),
    path('main-info/<int:pk>/', MainInfoByIdApiView.as_view()),
    path('category-for-page/',CategoriesForPagesListApiView.as_view()),
    path('category-for-page/create/', CategoriesForPagesCreateApiView.as_view()),
    path('category-for-page/<int:pk>/', CategoriesForPagesByIdApiView.as_view()),
    path('page/',PagesListApiView.as_view()),
    path('page/create/', PagesCreateApiView.as_view()),
    path('page/<int:pk>/', PagesByIdApiView.as_view()),
]