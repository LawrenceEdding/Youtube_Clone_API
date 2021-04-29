from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReplyList.as_view()),
    path('comment/<int:pk>', views.ReplyDetail.as_view())
]