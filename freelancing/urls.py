from django.contrib import admin
from django.urls import path,include
from login_logout import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',auth_views.LoginView.as_view(template_name='login_logout/login.html'),name="login"),
    path('logout/',auth_views.LogoutView.as_view(template_name='login_logout/logout.html'),name="logout"),
    path('',include('login_logout.urls')),
    path('register/',views.register, name="registration"),
    path('',include('blog.urls')),
    path('blog-home/',views.home),

]
