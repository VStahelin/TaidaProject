from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('AhoBox.urls')),
    path('', include('Users.urls')),
    path('', include('Anime.urls'))
]
