from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.generic.edit import FormView
from .forms import RegistrationForm, LoginForm


class RegistrationView(FormView):
    template_name = 'registration/register.html'
    form_class = RegistrationForm
    success_url = '/'
    
    def form_valid(self, form):
        name = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = User.objects.create_user(name, email, password)
        new_user = authenticate(username=name, password=password)
        login(self.request, new_user)
        return super(RegistrationView, self).form_valid(form)


class LoginView(FormView):
    template_name = 'registration/login.html'
    form_class = LoginForm
    success_url = '/'
    
    def form_valid(self, form):
        name = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=name, password=password)
        if user is not None:
            login(self.request, user)
        return super(LoginView, self).form_valid(form)


def logout_view(request):
    logout(request)
    return redirect('home')

