from django.urls import path
from . import views
from django.contrib import admin
app_name = 'board'
urlpatterns = [
    path('', views.thread_list, name='thread_list'),
    path('hello/', views.hello, name='hello'),
    path('tanukiti/', views.tanukiti, name='tanukiti'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),  # ←追加
    path('thread/create/', views.thread_create, name='thread_create'),  # ←追加
    path('search/', views.search, name='search'),
    path('search_results/', views.search_results, name='search_results'),
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
]