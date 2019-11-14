from django.urls import path,include
from .views import EmployeeListView, EmployeeDetailView, EmployeeUpdateView, EmployeeDeleteView
from core.api.views import save_emp
urlpatterns=[
    path('', save_emp),
    path('details',EmployeeListView.as_view()),
    path('employee/<pk>', EmployeeDetailView.as_view()),
    path('employee/<pk>/delete',EmployeeDeleteView.as_view()),
    path('employee/<pk>/update',EmployeeUpdateView.as_view()),
     
]
