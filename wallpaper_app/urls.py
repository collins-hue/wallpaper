from django.urls import path

from wallpaper_app import views


app_name = 'wallpaper_app'

urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('terms/', views.terms_condition, name='terms_condition'),
    path('contact/', views.contact_us, name='contact_us'),
    path('<int:id>/', views.wallpaper_info, name='wallpaper_info'),
]