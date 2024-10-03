from django.urls import path
from django.contrib import admin
from .views import availability, register, user_login, home, Assign, unlock
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('availability/', availability, name='availability'),
    path('assign/', Assign, name='assign'),
    path('unlock/', unlock, name='unlock'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', home, name='home'),
]