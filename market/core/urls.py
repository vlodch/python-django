from django.contrib.auth import views as auth_views
from django.urls import include, path
from django.views.generic import RedirectView


from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
    path("dashboard/", include('dashboard.urls', namespace='dashboard')),
    # path('', RedirectView.as_view(pattern_name='dashboard:index')),
    # path('dashboard/', include('dashboard.urls')),  # Assuming you have a separate urls.py for dashboard

]