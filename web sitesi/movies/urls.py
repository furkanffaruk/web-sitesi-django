from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name="home"),
    path('home/',views.home,name="homee"),
    path('movies/',views.movies,name="movies"),
    path('movies/<int:id>',views.movie_details,name="details"),
    path('kategoriler/Macera',views.macera,name="macera"),
    path('kategoriler/Dram',views.dram,name="dram"),
    path('kategoriler/Aksiyon',views.aksiyon,name="aksiyon"),
    path('kategoriler/Korku',views.korku,name="korku"),
    path('kategoriler/Gerilim',views.gerilim,name="gerilim")



]
