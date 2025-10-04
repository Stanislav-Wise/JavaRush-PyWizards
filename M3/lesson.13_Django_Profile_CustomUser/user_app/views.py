from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView, RedirectView, TemplateView, UpdateView
from .forms import CustomAuthenticationForm, CustomUserCreationForm, UserUpdateForm
from .models import CustomUser


class RegisterView(FormView):
    template_name = 'user_app/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'user_app/login.html'
    authentication_form = CustomAuthenticationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('profile')

    def get_success_url(self):
        return self.success_url


class CustomLogoutView(LogoutView):
    template_name = 'user_app/logout.html'
    next_page = reverse_lazy('login')


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user_app/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'user_app/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user