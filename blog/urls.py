from django.urls import path
from . import views


urlpatterns = [
    path('', views.posts_list, name='articles'),
    path('post/create/', views.PostCreate.as_view(), name='post_create'),  # должен быть сверху от нижнего
    path('post/<str:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<str:slug>/update/', views.PostUpdate.as_view(), name='post_update'),
    path('post/<str:slug>/delete/', views.PostDelete.as_view(), name='post_delete'),
    path('post/<int:pk>/comment/', views.PostCommentCreate.as_view(), name='post_comment'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),

#     path('tags/', tags_list, name='tags_list_url'),
#     path('tag/create/', TagCreate.as_view(), name='tag_create_url'),  # должен быть сверху от нижнего
#     path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
#     path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
#     path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),
]
