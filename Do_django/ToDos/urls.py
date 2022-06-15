from django.urls import path
from . import views

urlpatterns=[
  path('all-to-dos', views.AllToDos.as_view()),
  path('all-to-dos/<str:pk>', views.DetailedToDos.as_view()),
  path('completed', views.CompletedToDos.as_view()),
  path('active', views.ActiveToDos.as_view()),
]