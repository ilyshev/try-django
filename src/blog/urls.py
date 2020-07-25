from django.urls import path
from .views import (
	ArticleListView,
	ArticleDetailView
	)


app_name = 'articles'
urlpatterns = [
    # path('create/', ArticleListView.as_view(), name='article-create'),
    # path('product/', product_detail_view),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'), #pk!! not id
    # path('<int:id>/delete/', product_delete_view, name='article-delete'),
    path('', ArticleListView.as_view(), name='article-list'),
]