from django import views
from django.urls import path
from randomizer.views import DisplayView
from randomizer.views import MCView

urlpatterns = [
    path('display/', DisplayView.as_view()),
    path('mc/', MCView.as_view()),
#    path('', DisplayView.as_view()),
#    path('', views.index, name='index'),
]
