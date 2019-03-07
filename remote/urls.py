from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from remote.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('grupos/', include('grupos.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacs/', include('contacts.urls')),
    path('jsonfile/', include('jsonfile.urls')),
    path('', include(router.urls)), #snippets
    path('', include('snippets.urls')), #snippets
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')), #snippets
    path('api/user/', include('user.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

