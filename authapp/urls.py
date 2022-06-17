from django.urls import path
import authapp.views as authapp

app_name = 'authapp'

urlpatterns = [
    path('login/', authapp.login, name='login'),
    path('logout/', authapp.logout, name='logout'),
    path('register/', authapp.register, name='register'),
    path('profile/', authapp.edit_profile, name='profile'),
    # path('verify/<email>/<key>', authapp.verify, name='verify'),
]