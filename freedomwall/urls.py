from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rant.urls')),
    path('members/', include('django.contrib.auth.urls')), #import all auser authetication func in django //  django has built-in func
    path('members/', include('members.urls')),
]
