"""Food_Recipe_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from RecipeApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.MyRecipe.as_view(),name='home'),
    path('ShowRecipes/',views.ShowRecipe.as_view(),name='showRecipe'),
    path('AddRecipe/',views.AddRcp.as_view(),name='addRecipe'),
    path('EditRecipe/<int:id>',views.editrcp,name='editRecipe'),
    path('showOwner/<int:id>',views.visiteOwner,name='showOwner'),
    path('delete/<int:id>',views.deleterp,name='deleterp'),
    path('SignUp/',views.signup.as_view(),name='signUp'),
    path('SignIn/',views.signin.as_view(),name='signIn'),
    path('logout/',views.logoutuser,name='logout'),
    path('about/',views.aboutpage,name='about'),
]
