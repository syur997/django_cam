from django.urls import path
from .views import *
from . import views
import cv2
import datetime


urlpatterns = [
   # path('', index, name='index')
    path('', fileUpload, name='fileupload'),
    path('receive/', fileReceive),
    path('',views.home,name="home"), # 웹사이트 링크 home.html
    path("camera/",views.detectme,name="camera"),




    # path('all/', CategoryViewSet.as_view(
    #     {
    #         'get':'list',
    #         'post':'create',
    #     }
    # )),
    # path('all/<int:pk>/', CategoryViewSet.as_view(
    #     {
    #         'get':'retrieve',
    #         'put':'partial_update',
    #         'delete':'destroy',
    #     }
    # )),

    # path('amenities/', Amenities.as_view()),

    # path('amenities/<int:pk>/', AmenityDetail.as_view()),

    # path('test/', Rooms.as_view()),
]

