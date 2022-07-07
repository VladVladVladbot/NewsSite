from django.urls import path
from news.views import *

urlpatterns = [
    path('wot/', wot, name='wot' ),
    path('test/', test, name='test'),
    path('login/', user_login, name='login'),
    path('logiout/', user_logout, name='logout'),
    path('register/', register, name='register'),
    path('', HomeNews.as_view(), name='index'),
    path('category/<int:category_id>/', CategoryHome.as_view(), name='category'),
    path('news/<int:pk>/', View_newsHome.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news'),
]

