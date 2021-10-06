from django.contrib import admin
from django.urls import path

#CUSTOM IMPORT
from django.conf import settings
from django.conf.urls.static import static
from products import views as pro
from accounts import views as acc

urlpatterns = [
    path('admin/', admin.site.urls),
    #CUSTOM URLS
    #URLS FOR ADMIN PANNEL
    path('dashboard/', pro.AdminDashBoardView, name="admin-dashboard" ),
    path('admin/', acc.AdminLoginView, name="loginpage" ),
    path('admin_login_process/', acc.AdminLoginProcess, name="admin-login-process" ),
    path('admin_logout_process/', acc.AdminLogoutProcress, name="admin-logout-process" ),
    #URLS FOR SITE FRONTEND
    path('', pro.FrontEndView, name="front-end-index"),
    path('costomer_login_process/', acc.CustomerLoginProcress, name="costomer-login-process"),
    path('costomer_registration_process/', acc.CustomerRegistrationView, name="costomer-registration-process"),
    path('costomer_logout_process/', acc.CustomerLogoutProcess, name="costomer-logout-process"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


