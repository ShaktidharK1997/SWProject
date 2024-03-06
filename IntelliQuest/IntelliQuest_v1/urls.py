from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from .views import login_view


#Routing basic search to search_results view
urlpatterns = [
    path('search/', views.search_articles, name='search_articles'),
    path('paper/', views.get_paper_info, name= 'search_paper'),
    path('accounts/', include('django.contrib.auth.urls')),
    #path('accounts/', include('allauth.urls')),
    #path('accounts/login/', login_view, name='api_login'),
]


