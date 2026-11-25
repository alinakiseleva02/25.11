from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.ServiceListView.as_view(), name='main'),
    path('services/', views.ServiceListView.as_view(), name='services'),
    path('account/', views.PersonalAccountView.as_view(), name='account'),
    path('create-request/', views.RequestCreateView.as_view(), name='create_request'),
    path('my-login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='main'), name='logout'),
]