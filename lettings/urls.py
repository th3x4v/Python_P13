from django.contrib import admin
from django.urls import path

from lettings.views import index, letting

urlpatterns = [
    path('lettings/', index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='letting'),
]