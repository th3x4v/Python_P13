from django.contrib import admin
from django.urls import path
from lettings.views import index, letting
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('lettings/', index, name='lettings_index'),
    path('lettings/<int:letting_id>/', letting, name='letting'),
]


handler404 = 'oc_lettings_site.views.handler404'
handler500 = 'oc_lettings_site.views.handler500'