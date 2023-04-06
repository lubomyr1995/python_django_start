from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('auth', include('apps.auth.urls')),
    path('users', include('apps.users.urls')),
    path('auto_parks', include('apps.auto_parks.urls')),
    path('cars', include('apps.cars.urls'))
]

handler400 = 'rest_framework.exceptions.bad_request'
handler500 = 'rest_framework.exceptions.server_error'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
