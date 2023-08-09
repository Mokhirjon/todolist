from django.urls import path
from .views import (TodolistALLView,DetailTodolistsView,
                    CreateTodolistViews,UpdateTodolistView,DeleteToDoListView)
urlpatterns=[
    path('get_all/',TodolistALLView.as_view()),
    path('get_by_index/<int:todolist_id>',DetailTodolistsView.as_view()),
    path('create/',CreateTodolistViews.as_view()),
    path('update/<int:todolist_id>/',UpdateTodolistView.as_view()),
    path ('delete/<int:todolist_id>/',DeleteToDoListView.as_view()),
]