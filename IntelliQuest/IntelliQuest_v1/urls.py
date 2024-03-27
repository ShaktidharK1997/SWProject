from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

from .views import PersonalInfoView, EducationViewSet, upload_profile_picture


#Routing basic search to search_results view
urlpatterns = [
    path('search/', views.search_articles, name='search_articles'),
    path('paper/', views.get_paper_info, name= 'search_paper'),
    path('signin/', views.sign_in, name='sign_in'),
    path('signup/', views.sign_up, name='sign_up'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    #Shivaji Paths
    path('personalinfo/<str:username>/', PersonalInfoView.as_view(), name='personalinfo-by-username'),
    path('upload_profile_picture/<str:username>/', upload_profile_picture, name='upload-profile-picture'),
    path('personalinfo/', PersonalInfoView.as_view(), name='personal-info'),
    path('education/',EducationViewSet.get_queryset)
]
