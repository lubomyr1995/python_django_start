from django.urls import path

from users.views import UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('users', UserListCreateView.as_view(), name='user_list_create'),
    path('users/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_destroy')
]
