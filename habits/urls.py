from django.urls import path
from habits import views

urlpatterns = [
    path('habits/', views.HabitList.as_view()),
    path('habits/<int:pk>/', views.HabitDetail.as_view())
]
