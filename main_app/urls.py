from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('guitars/', views.guitars_index, name='guitars_index'),
    path('guitars/<int:guitar_id>/', views.guitars_detail, name='guitars_detail'),
    path('guitars/create/', views.GuitarCreate.as_view(), name='guitars_create'),
    path('guitars/<int:pk>/update/', views.GuitarUpdate.as_view(), name='guitars_update'),
    path('guitars/<int:pk>/delete/', views.GuitarDelete.as_view(), name='guitars_delete'),
    path('guitars/<int:guitar_id>/add_practice/', views.add_practice, name='add_practice'),
    path('guitars/<int:guitar_id>/add_photo/', views.add_photo, name='add_photo'),
    path('guitars/<int:guitar_id>/assoc_case/<int:case_id>/', views.assoc_case, name='assoc_case'),
    path('guitars/<int:guitar_id>/remove_case/<int:case_id>/', views.remove_case, name='remove_case'),
    path('cases/', views.cases_index, name='cases_index'),
    path('cases/<int:case_id>', views.cases_detail, name='cases_detail'),
    path('cases/create/', views.CaseCreate.as_view(), name='cases_create'),
    path('cases/<int:pk>/update/', views.CaseUpdate.as_view(), name='cases_update'),
    path('cases/<int:pk>/delete/', views.CaseDelete.as_view(), name='cases_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]