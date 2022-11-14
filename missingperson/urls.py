
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app import views

urlpatterns = [
    path('', views.addElement, name="start"),
    path('compare/', views.compareElement, name="compare"),
    path('executeCompare', views.executeCompare),
    path('delete_all', views.delete_all),
    path('admin/', admin.site.urls)
    
] + static (settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))