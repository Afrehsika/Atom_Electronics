"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from config import views

# Set up the DRF router
from periodic_table.views import ElementViewSet
from users.views import UserViewSet, StudentProfileViewSet
from simulations.views import BondViewSet, MaterialViewSet
from learning.views import LessonViewSet, QuizViewSet, StudentProgressViewSet

router = DefaultRouter()
router.register(r'elements', ElementViewSet)
router.register(r'users', UserViewSet)
router.register(r'profiles', StudentProfileViewSet)
router.register(r'bonds', BondViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'lessons', LessonViewSet)
router.register(r'quizzes', QuizViewSet)
router.register(r'progress', StudentProgressViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', views.index, name='index'),
    path('simulations/', views.simulations, name='simulations'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('atom-viewer/', views.atom_viewer, name='atom_viewer'),
    path('atom-builder/', views.atom_builder, name='atom_builder'),
    path('learning/', views.learning, name='learning'),
    path('learning/lesson/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('learning/game/conductivity/', views.learning_game, name='learning_game'),


    path('api/recipes/', views.recipes_api, name='recipes_api'),
]
