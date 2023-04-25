from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    path("login/", views.LoginView.as_view(template_name="cadastros/form.html"), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout")
]
