from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.home.urls', namespace='home')),
    path('login/', include('core.login.urls', namespace='login')),
    path('usuarios/', include('core.users.urls', namespace='users')),
    path('campusvirtual/', include('core.campus.urls', namespace='campus')),
]