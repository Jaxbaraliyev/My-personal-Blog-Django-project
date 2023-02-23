from django.contrib import admin
from django.urls import path
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about),
    path('blog/', blog),
    path('maqola/<int:pk>/', maqola, name="maqola"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


