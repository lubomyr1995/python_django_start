from django.urls import path

from users.views import UserLiltCreateView, UserRetrieveUpdateDestroyView


urlpatterns = [
    path('users', UserLiltCreateView.as_view(), name='user_list_create'),
    path('users/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_destroy')
]
