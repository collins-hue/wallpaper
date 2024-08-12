from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from wallpaper import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('wallpaper_app.urls', namespace='wallpaper_app')),
    
]
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
