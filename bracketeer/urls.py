from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

import debug_toolbar

urlpatterns = [
    path('', include('bracket.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
