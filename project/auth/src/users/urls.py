from django.urls import path, include

from users import views


urlpatterns = [
    path('users/login/', views.user_login, name='login'),
    path('users/logout/', views.UserLogout.as_view(), name='logout'),
    path('users/current/', views.CurrentUser.as_view()),
    path('profile/', views.user_profile, name='profile'),
]
