from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:teacher_id>/', views.detail, name='detail'),
    path('import/', views.importer, name='importer'),
    path('success/', views.import_success, name='import_success'),
]