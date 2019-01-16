from django.urls import path
from . import views

urlpatterns = [
    # path('profiles/', views.ProfilesListView.as_view(), name='profiles'),
    # path('profile/<int:pk>/', views.ProfileDetailView.as_view(), name='profile-detail'),
    # path('profile/<int:pk>/update/', views.ProfileCreate.as_view(), name='update-profile'),
    path('registration/', views.register, name='user-registration'),
]
