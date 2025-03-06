from django.urls import path

from .views import GetTaskInfoView

urlpatterns = [
    path('tasks/', GetTaskInfoView.as_view()),
]
