from django.urls import path
from . import views


urlpatterns = [
    path('', views.ReplyList.as_view()),
    path('<int:pk>', views.ReplyDetail.as_view())
]