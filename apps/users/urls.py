from django.urls import path

from .views import UserListView, UserToAdminView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user_to_admin'),
]
