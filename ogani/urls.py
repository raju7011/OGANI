from django.contrib import admin
from django.urls import path

#CUSTOM IMPORT
from django.conf import settings
from django.conf.urls.static import static
from products import views as pro

urlpatterns = [
    path('admin/', admin.site.urls),
    #CUSTOM URLS
    #URLS FOR ADMIN PANNEL
    path('ogani_dashboard/', pro.AdminDashBoardView, name="admin-dashboard" ),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

