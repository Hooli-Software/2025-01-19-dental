from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),  # Админка вне i18n_patterns
]

urlpatterns += i18n_patterns(
    path('set-language/', include('django.conf.urls.i18n')),
    path('', include('apps.base.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
