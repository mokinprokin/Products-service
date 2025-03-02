"""
URL configuration for study_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView, CreateView
from editor.views.views import (
    filters,
    Registration,
    Login,
    change_password,
    home,
    logout,
    detail,
    profile,
    edit_host,
    chats,
    chat
)
from study_django.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static

authentification_patterns = [
    path("", Login.as_view(), name="login"),
    path("logout/", logout, name="logout"),
    path("registration/", Registration.as_view(), name="registration"),
    re_path("^change", change_password, name="change_password"),
]
menu_patterns = [
    path("home", home, name="home"),
    path("about", home, name="about"),
    path("search", home, name="search"),
    path("profile", profile, name="profile"),
]
chat_patterns = [
    path("chats", chats, name="chats"),
    re_path("chats/(?P<id>[0-9]+)$", chat, name="chat"),
]
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(authentification_patterns)),
    path("filters", filters, name="filters"),
    path("account/user/", include(menu_patterns)),
    re_path("account/user/detail/(?P<id>[0-9]+)$", detail, name="detail"),
    re_path("account/user/edit/(?P<id>[0-9]+)$", edit_host, name="edit_host"),
    path("account/user/profile/",include(chat_patterns)),
]
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
