from django.urls import path
from .views import homePageView, AboutPageView

urlpatterns = [
    path("", homePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about')
]