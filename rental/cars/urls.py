from django.urls import path

from .views import PersonView, PersonDetail, RegisterUser

urlpatterns = [
    path('', PersonView.as_view(), name='home'),
    path('person/<int:pk>/', PersonDetail.as_view(), name='1'),
    path('register/', RegisterUser.as_view(), name='register'),
]
