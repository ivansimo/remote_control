from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static




from rest_framework.urlpatterns import format_suffix_patterns
from devs import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('grupos/', include('grupos.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacs/', include('contacts.urls')),
    path('jsonfile/', include('jsonfile.urls')),
    path('devices/', views.DeviceList.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)