from django.urls import path
from profiles.views import index, profile
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('profiles/', index, name='profiles_index'),
    path('profiles/<str:username>/', profile, name='profile'),
]

handler404 = 'oc_lettings_site.views.handler404'
handler500 = 'oc_lettings_site.views.handler500'