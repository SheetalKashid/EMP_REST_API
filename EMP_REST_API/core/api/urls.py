from django.urls import path,include
from .views import EmployeeListView, EmployeeDetailView
from core.api.views import save_emp
urlpatterns=[
    path('', save_emp),
    path('details',EmployeeListView.as_view()),
    path('<pk>', EmployeeDetailView.as_view()), 
]
