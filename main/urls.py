from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:category_id>/', views.get_article_by_category, name='get_article_by_category'),
    path('tag/<int:tag_id>/', views.get_article_by_tag, name='get_article_by_tag'),
    path('create_article/', views.create_article, name='create_article'),
    path('article/<int:article_id>/', views.detail_article, name='detail_article'),
    path('add_category/', views.add_category, name='add_category'),
    path('delete_article/<int:article_id>/', views.delete_article, name='delete_article'),
    path('edit_article/<int:article_id>/', views.edit_article, name='edit_article'),
    path('add_comment/<int:pk>/', views.add_comment, name='add_comment'),
    path('delete_comment/<int:article_id>/<int:comment_id>', views.delete_comment, name='delete_comment'),
    path('like_article/<int:pk>/', views.like_article, name='like_article'),

]
