from django.urls import path
from . import views

urlpatterns = [
  path('', views.generative_agriculture, name='generative_agriculture'),
  path('soil_practices/', views.soil_practices, name='soil_practices'),
  path('soil_solutions/', views.soil_solutions, name='soil_solutions'),
  path('soil_effects/', views.soil_effects, name='soil_effects'),
  path('cover_types/', views.cover_types, name='cover_types'),
  path('root_practices/', views.root_practices, name='root_practices'),
  path('diverse_strategies/', views.diverse_strategies, name='diverse_strategies'),
  path('diverse_benefits/', views.diverse_benefits, name='diverse_benefits'),
  path('diverse_limitations/', views.diverse_limitations, name='diverse_limitations'),
  path('livestock_benefits/', views.livestock_benefits, name='livestock_benefits'),
  path('livestock_limitations/', views.livestock_limitations, name='livestock_limitations'),
]