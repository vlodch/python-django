from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import views

urlpatterns = [
    path("", include('core.urls')),
    path("items/", include('item.urls')),
    # path("dashboard/", include('dashboard.urls')),
    path("dashboard/", include('dashboard.urls')),
    path("inbox/", include('conversation.urls')),
    path('contact/', views.contact, name='contact'),
    path("admin/", admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)