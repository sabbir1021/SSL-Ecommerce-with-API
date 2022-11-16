from django.urls import path
from . import views
app_name = "payments"

urlpatterns = [
    path('', views.Payment.as_view(), name="payment"),
    path('status/', views.Status.as_view(), name="status")
]
