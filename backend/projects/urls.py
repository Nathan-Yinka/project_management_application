from django.urls import path
from .views import (
    ProjectListCreateView,
    ProjectDetailView,
    UpdateProjectStatus,
    AddCommentView,
)

urlpatterns = [
    # URL for listing all projects or creating a new project
    path('', ProjectListCreateView.as_view(), name='project-list-create'),

    # URL for retrieving, updating, or deleting a specific project
    path('<int:pk>/<int:organization_id>/', ProjectDetailView.as_view(), name='project-detail'),

    # URL for updating the status of a project
    path('<int:project_id>/update-status/', UpdateProjectStatus.as_view(), name='update_project_status'),

    # URL for adding a comment to a specific project
    path('<int:project_id>/add-comment/', AddCommentView.as_view(), name='project-add-comment'),
]
