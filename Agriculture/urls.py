from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
#   path('about/', views.about, name='about'),
#   path('contact/', views.contact, name='contact'),
#   path('services/', views.services, name='services'),
#   path('products/', views.products, name='products'),
#   path('news/', views.news, name='news'),
#   path('blog/', views.blog, name='blog'),
#   path('faq/', views.faq, name='faq'),
#   path('gallery/', views.gallery, name='gallery'),
#   path('careers/', views.careers, name='careers'),
#   path('subscribe/', views.subscribe, name='subscribe'),
#   path('faq-details/', views.faq_details, name='faq-details'),
#   path('blog-details/', views.blog_details, name='blog-details'),
]