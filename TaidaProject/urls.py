from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.AhoBox.urls')),
    path('', include('apps.Users.urls')),
    path('', include('apps.Anime.urls')),
    path('', include('apps.Lists.urls'))
]
