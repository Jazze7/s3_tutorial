from web import views
from django.urls import path, include


app_name = "web"


urlpatterns = [
    path('upload-image/', views.upload, name="upload"),
    path('', views.index, name="index"),

]