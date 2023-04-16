from django.urls import path

from .views import (
    AdminToUserView,
    UserActiveView,
    UserBlockView,
    UserListView,
    UserProfileUpdateView,
    UserRetrieveDestroyView,
    UserToAdminView,
)

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('/profile', UserProfileUpdateView.as_view(), name='user_profile_update'),
    path('/<int:pk>', UserRetrieveDestroyView.as_view(), name='user_retrieve_destroy'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user_to_admin'),
    path('/<int:pk>/to_user', AdminToUserView.as_view(), name='admin_to_user'),
    path('/<int:pk>/to_block', UserBlockView.as_view(), name='user_un_active'),
    path('/<int:pk>/to_active', UserActiveView.as_view(), name='user_active')
]
