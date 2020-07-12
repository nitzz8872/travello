from django.urls import path,include
from travello_app import views


urlpatterns = [
    path('',views.xyz,name="xyz")
]
