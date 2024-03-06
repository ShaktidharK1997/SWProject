from django.urls import path, re_path, include
from .views import home, login_view, FrontendAppView  # Ensure FrontendAppView is imported here

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/login/', login_view, name='api_login'),
    #re_path(r'^accounts/login/?$', FrontendAppView.as_view()),
]