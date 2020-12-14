from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.multimeter, name='certificateofmultimeter'),
    path('listview/', views.CertificateList.as_view(), name='listcert'),
    path('<pk>/', views.CertificateDetail.as_view(), name='detailcert'),
]