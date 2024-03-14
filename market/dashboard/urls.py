# urls.py
from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
]



# urlpatterns = [
#     path('dashboard/', views.dashboard, name='dashboard:index'),
#     # Other URL patterns
# ]

#dashboard/urls.py

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.dashboard, name='index'),
# ]

# from django.urls import path, include

# urlpatterns = [
#     path('dashboard/', include('dashboard.urls', namespace='dashboard')),
#     # Other URL patterns...
# ]
