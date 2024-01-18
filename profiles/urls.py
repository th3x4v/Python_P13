from django.urls import path

from profiles.views import index, profile

urlpatterns = [
    path('profiles/', index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),
]
