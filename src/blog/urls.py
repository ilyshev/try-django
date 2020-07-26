from django.urls import path
from .views import (
	ArticleCreateView,
	ArticleDetailView,
	ArticleDeleteView,
	ArticleListView,
	ArticleUpdateView
	)


app_name = 'articles'
urlpatterns = [
	path('', ArticleListView.as_view(), name='article-list'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
    path('<int:id>/update', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'), #pk!! not id if there isn't def get_object() in .views
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    
]