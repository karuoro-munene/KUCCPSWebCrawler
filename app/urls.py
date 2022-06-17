from django.urls import path
from app import views

urlpatterns=[
    path('', views.APIRoot.as_view()),
    path('api/v1/institutions', views.institutions),
    path('api/v1/programme/details', views.programme_details),
]