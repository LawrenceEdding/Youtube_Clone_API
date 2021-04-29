from django.urls import path
from . import views


urlpatterns = [
    path('', views.CommentList.as_view()),
    path('comment/<int:pk>', views.CommentDetail.as_view())
]