from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:pk>', views.profile_view, name='profile'),
    path('autorizationedit_profile/<int:pk>', views.edit_profile, name='edit_profile')

]