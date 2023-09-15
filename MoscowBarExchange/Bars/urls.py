from django.urls import path

from .views import index, index_dark, about, about_dark, register, register_dark, user_logout, user_logout_dark

urlpatterns = [
    path('', index, name='home'),
    path('dark/', index_dark, name='home_dark'),
    path('register/', register, name='register'),
    path('register/dark/', register_dark, name='register_dark'),
    path('logout/', user_logout, name='logout'),
    path('logout/dark/', user_logout_dark, name='logout_dark'),
    path('about_us/', about, name='about'),
    path('about_us/dark/', about_dark, name='about_dark'),
]
