from django.urls import path
from app.views.project import (
    ProjectCreateView, ProjectListView, ProjectDetailView,
    ProjectUpdateView, ProjectDeleteView
)
from app.views.todo import (
    TodoCreateView, TodoListView, TodoDetailView,
    TodoUpdateView, TodoDeleteView,
)
from app.views.comment import (
    CommentCreateView, CommentListView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    # Project
    path('projects/', ProjectListView.as_view()),
    path('projects/create/', ProjectCreateView.as_view()),
    path('projects/<int:pk>/', ProjectDetailView.as_view()),
    path('projects/<int:pk>/update/', ProjectUpdateView.as_view()),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view()),

    # Todo
    path('todos/', TodoListView.as_view()),
    path('todos/create/', TodoCreateView.as_view()),
    path('todos/<int:pk>/', TodoDetailView.as_view()),
    path('todos/<int:pk>/update/', TodoUpdateView.as_view()),
    path('todos/<int:pk>/delete/', TodoDeleteView.as_view()),

    path('todos/<int:todo_id>/comments/', CommentCreateView.as_view(), name='comment-create'),
    path('todos/<int:todo_id>/comments/list/', CommentListView.as_view(), name='comment-list'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
]


