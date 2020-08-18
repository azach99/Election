from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_list, name = 'Users-list'),
    path('<slug:slug>/', views.SubmissionDetail.as_view(), name = 'Users-specifics'),
    #path('profile/', views.profile, name = 'profile'),
]