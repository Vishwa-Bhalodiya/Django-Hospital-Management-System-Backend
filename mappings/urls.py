from django.urls import path
from .views import (
    MappingListCreateView,
    MappingByPatientView,
    MappingDetailView
)

urlpatterns = [
    path('', MappingListCreateView.as_view(), name='mapping-list-create'),
    path('patient/<int:patient_id>/', MappingByPatientView.as_view(), name='mapping-by-patient'),
    path('<int:pk>/', MappingDetailView.as_view(), name='mapping-detail'),
]
