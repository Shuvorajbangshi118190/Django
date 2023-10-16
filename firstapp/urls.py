from django.urls import path
from .views import *
from .registration import *

urlpatterns =[
    path('first/',firstAPI,name='first'),
    path('registration/',registrationAPI),
    path('classbased/',ContactAPIView.as_view()),
    path('post/',PostCreateAPIView.as_view()),
]