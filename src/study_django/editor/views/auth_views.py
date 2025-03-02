from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from editor.models import User, UserProfile
from editor.forms.auth_forms import UserRegistrationForm
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.sessions.models import Session
from django.contrib.auth import logout as user_logout
from django.contrib.auth.decorators import login_required
from study_django.settings import LOGIN_REDIRECT_URL
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.sessions.models import Session
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


class Login(LoginView):
    model = User
    template_name = "login.html"
    extra_context = {"title": "Вход"}
    success_url = "home"

    def dispatch(self, request, *args, **kwargs):
        if check_session_view(request, self.success_url):
            return redirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)


class Registration(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = "registration.html"
    success_url = reverse_lazy("home")
    extra_context = {"title": "Регистрация"}


def check_session_view(request, name_path):
    session_id = request.COOKIES.get("sessionid")  # Получаем session_id из куки

    # Проверяем, существует ли сессия
    try:
        session = Session.objects.get(session_key=session_id)
        user_id = session.get_decoded().get("_auth_user_id")

        # Проверяем, зарегистрирован ли пользователь
        User = get_user_model()
        user = User.objects.get(pk=user_id)

        return user

    except:
        pass


@login_required
def logout(request):
    user_logout(request)
    return redirect(LOGIN_REDIRECT_URL)


def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Your password was successfully updated!")
            return redirect("home")
        else:
            messages.error(request, "Please correct the error below.")
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "change_password.html", {"form": form})
