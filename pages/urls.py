from django.urls import path 

from .views import HOmePageView

urlpatterns = [
    path('', HOmePageView.as_view(), name='home')
]
