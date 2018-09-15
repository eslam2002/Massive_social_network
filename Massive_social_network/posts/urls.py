from django.urls import path
from .views import *

app_name = 'post'

urlpatterns = [
    path('',PostListView.as_view(),name='list'),
    path('create/',PostCreatView.as_view(),name='create'),
    path('<int:pk>/update/',PostUpdateView.as_view(),name='update'),
    path('<int:pk>/delete/',PostDeleteView.as_view(),name='delete'),
    path('<username>/',UserDetailView.as_view(), name='detail'),  

]
