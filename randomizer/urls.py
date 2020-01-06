from django import views
from django.urls import path
from randomizer.views import DisplayView
from randomizer.views import MCView
from randomizer.views import SpotlightView
from randomizer.views import SpotlightDancerView
from randomizer.views import SpotlightMCView
from randomizer.views import SpotlightResetView
from django.contrib import admin

# Admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('display/', DisplayView.as_view()),
    path('mc/', MCView.as_view()),
    path('spotlight/', SpotlightView.as_view()),
    path('spotlight_dancer/', SpotlightDancerView.as_view()),
    path('spotlight_mc/', SpotlightMCView.as_view()),
    path('spotlight_reset/', SpotlightResetView.as_view()),

]
