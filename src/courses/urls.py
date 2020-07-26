from django.urls import path
from .views import (
	CourseListView,
	CourseView,
	# my_fbv
)


app_name = 'courses'
urlpatterns = [
	path('', CourseListView.as_view(), name='courses-list'),
	# path('', my_fbv, name='courses-list')
 #    path('create/', CourseCreateView.as_view(), name='course-create'),
    # path('<int:id>/update', ArticleUpdateView.as_view(), name='article-update'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'), #pk!! not id if there isn't def get_object() in .views
    # path('<int:id>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    
]