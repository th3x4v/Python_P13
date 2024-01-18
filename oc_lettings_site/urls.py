from django.contrib import admin
from django.urls import path, include

from oc_lettings_site.views import index

urlpatterns = [
    path('',index, name='index'),
    path("", include("lettings.urls")),
    path("", include("profiles.urls")),
    path('admin/', admin.site.urls),
]


from django.conf.urls import handler404, handler500

handler404 = 'oc_lettings_site.views.handler404'
handler500 = 'oc_lettings_site.views.handler500'