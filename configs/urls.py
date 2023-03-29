from django.urls import path, include

urlpatterns = [
    path('auth', include('apps.auth.urls')),
    path('users', include('apps.users.urls')),
    path('auto_parks', include('apps.auto_parks.urls')),
    path('cars', include('apps.cars.urls'))
]
