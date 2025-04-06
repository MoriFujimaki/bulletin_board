from django.urls import path
from . import views
app_name = 'board'
urlpatterns = [
    path('', views.thread_list, name='thread_list'),
    path('hello/', views.hello, name='hello'),
    path('tanukiti/', views.tanukiti, name='tanukiti'),
    path('thread/<int:thread_id>/', views.thread_detail, name='thread_detail'),  # ←追加
    path('thread/create/', views.thread_create, name='thread_create'),  # ←追加
]