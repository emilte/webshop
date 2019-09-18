# imports
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required, user_passes_test
from django.db.models import Q
from django.urls import reverse
from accounts.forms import * # EmailForm, SignUpForm, CustomAuthenticationForm, EditUserForm, CustomPasswordChangeForm
from django.views import View
from django.contrib.auth import get_user_model
User = get_user_model()
# End: imports -----------------------------------------------------------------

class Home(View):
    template = 'webshop/home.html'
    def get(self, request):
        return render(request, self.template)
