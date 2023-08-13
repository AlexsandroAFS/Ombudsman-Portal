from django.urls import path
from . import views

urlpatterns = [
    path('', views.OmbudsmanPForm.as_view(), name='OmbudsmanPortal'),
]