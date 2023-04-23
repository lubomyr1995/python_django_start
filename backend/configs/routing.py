from django.urls import path

from channels.routing import URLRouter

from apps.auto_parks.routing import websocket_urlpatterns as auto_parks_routing

websocket_urlpatterns = [
    path('api/auto_parks', URLRouter(auto_parks_routing))

] 
