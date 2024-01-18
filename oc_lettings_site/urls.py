from django.contrib import admin
from django.urls import path

from lettings.views import lettings_index, letting
from profiles.views import profiles_index, profile
from oc_lettings_site.views import index

urlpatterns = [
    path('',index, name='index'),
    path('lettings/', lettings_index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='letting'),
    path('profiles/', profiles_index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),
    path('admin/', admin.site.urls),
]
