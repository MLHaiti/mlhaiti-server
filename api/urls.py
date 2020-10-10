from django.urls import path
from . import views

urlpatterns = [
	# USER END-POINTS
    path('users', views.UserList.as_view()),
    path('user/list', views.UserList.as_view()),

    path('forums', views.ForumList.as_view()),    
    path('forum/list', views.ForumList.as_view()),    
    # path('forum/<str:code>/messages', views.ForumMessagesList.as_view()),
    # path('forum/<str:code>/message/list', views.ForumMessagesList.as_view()),
]