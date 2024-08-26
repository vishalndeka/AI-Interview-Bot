from django.urls import path
from . import views

urlpatterns = [
    path("interviews/", views.InterviewListCreate.as_view(), name="interview_list"),
    path("interviews/delete/<int:pk>/", views.InterviewDelete.as_view(), name='delete-interview')
]