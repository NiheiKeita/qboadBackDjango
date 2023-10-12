from django.urls import path,include
from apiapp import apis
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('api/', include(apis.router.urls)),
]