from django import views
from django.urls import path
from randomizer.views import DisplayView

urlpatterns = [
    path('display/', DisplayView.as_view()),
#    path('', DisplayView.as_view()),
#    path('', views.index, name='index'),
]
