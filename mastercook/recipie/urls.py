from django.contrib import admin
from django.urls import path

from . import views

from django.contrib import admin
from django.urls import path, include


from .views import Listrecipie, DetailView, RecipeCreate, RecipeUpdateView, RecipeDeleteView, profileUpdateView, \
    profileDeleteView, profileDetailView, profileCreate, searchrecipie, data

urlpatterns = [

    path('create_recipie/', RecipeCreate.as_view(), name='recipiecreate'),
    path('list_recipie/', Listrecipie.as_view(), name='recipielist'),
    path('api/recipes/', searchrecipie.as_view(), name='recipiesearch'),
    path('details-view/<int:pk>/', DetailView.as_view(), name='details'),
    path('update-view/<int:pk>/', RecipeUpdateView.as_view(), name='update'),
    path('delete-view/<int:pk>/', RecipeDeleteView.as_view(), name='delete'),
    path('Detail/<int:pk>/',views.Detail,name='Detail'),
    path('create_profile/', profileCreate.as_view(), name='Profilecreate'),
    path('details-view-profile/<int:pk>/', profileDetailView.as_view(), name='Profiledetails'),
    path('update-view-profile/<int:pk>/', profileUpdateView.as_view(), name='Profileupdate'),
    path('delete-view-profile/<int:pk>/', profileDeleteView.as_view(), name='Profiledelete'),
    path('Profile-Detail/<int:pk>/', views.Detailprofile, name='profileDetail'),
    path('profile-create/', views.create_profile, name='profilecreate'),
    path('Profile-update/<int:pk>/', views.update_profile, name='profileupdate'),
    path('Profile-delete/<int:pk>/', views.delete_profile, name='profiledelete'),
    path('recipie-create/', views.create_recipe, name='recipiecreate'),
    path('recipie-update/<int:pk>/', views.update_recipie, name='recipieupdate'),
    path('recipie-delete/<int:pk>/', views.delete_recipie, name='recipieedelete'),
    path('DATA/', data.as_view(), name='data_'),
    path('userid', views.Userid, name='user_id'),

]

