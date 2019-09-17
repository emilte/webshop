# imports
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from accounts import views
from accounts.forms import CustomAuthForm
# End: imports -----------------------------------------------------------------

app_name = 'accounts' # Necessary for url naming. eg {% url 'accounts:signin' %}

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', LoginView.as_view(template_name='accounts/login.html', authentication_form=CustomAuthForm), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('change_password/', views.change_password, name='change_password'),

    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/settings', views.settings, name='settings'),

    path('delete_user/', views.delete_user, name="delete_user"),
]
