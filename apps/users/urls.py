from django.urls import path

from .views import (
    AdminToUserView,
    UserAddAvatarView,
    UserIsActiveForAdminsView,
    UserIsDeactivateForAdminsView,
    UserListView,
    UserRetrieveUpdateDestroyView,
    UserToAdminView,
)

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_destroy'),
    path('/avatars', UserAddAvatarView.as_view(), name='user_add_avatar'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user_to_admin'),
    path('/<int:pk>/to_user', AdminToUserView.as_view(), name='admin_to_user'),
    path('/<int:pk>/is_active', UserIsActiveForAdminsView.as_view(), name='user_active'),
    path('/<int:pk>/is_deactivate', UserIsDeactivateForAdminsView.as_view(), name='user_deactivate'),
]
