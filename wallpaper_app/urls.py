from django.urls import path

from wallpaper_app import views


app_name = 'wallpaper_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('wallpaper/<int:id>/', views.wallpaper_info, name='wallpaper_info'),
    path('about_us/', views.about_us, name='about_us'),
    path('buy_us_coffee/', views.buy_us_coffee, name='buy_us_coffee'),
    path('terms/', views.terms_condition, name='terms_condition'),
    path('contact/', views.contact_us, name='contact_us'),

]