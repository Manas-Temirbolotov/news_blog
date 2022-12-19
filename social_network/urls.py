from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('post', views.PostViewSet),
# router.register('comment', views.GenericAPIView),

urlpatterns = [
    path('comment/', views.CommentListCreateView.as_view(), name='comment_list'),
    path('comment/<int:pk>/', views.CommentRetrieveUpdateDestroyAPIView.as_view(), name='comment_detail'),
    path('', include(router.urls)),
]
