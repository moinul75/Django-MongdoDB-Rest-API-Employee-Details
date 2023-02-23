from django.urls import re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings


# set urls patterns 
urlpatterns = [
    re_path(r'^department$',views.DepartmentAPI),
    re_path(r'^department/([0-9]+)$',views.DepartmentAPI),
    re_path(r'^employee$',views.EmployeeAPI),
    re_path(r'^employee/([0-9]+)$',views.EmployeeAPI),
    re_path(r'^employee/photo',views.FIleAPI),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
