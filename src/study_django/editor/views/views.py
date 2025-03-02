from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from editor.views.auth_views import *
from editor.models import (
    UserProfile,
    HostItem,
    HostItemImages,
    Message,
    Chats,
    Feedback,
)
from editor.views.view_models.nav_item import NavigationItem
from editor.forms.profile_forms import UserProfileForm, UserHostForm, UserHostEditForm
from editor.views.view_models.profile_user_dto import ProfileUserDTO
from editor.views.view_scripts.profile_script import (
    rename_image,
    rename_image_host,
    rename_images_host,
)
from editor.forms.detail_forms import RewiewForm

MENU = [
    NavigationItem("Главная", "home"),
    NavigationItem("Поиск", "search"),
    NavigationItem("Профиль", "profile"),
    NavigationItem("Обращения", "chats"),
    NavigationItem("Выйти", "logout"),
]


@login_required
def filters(request):
    context = {
        "float": 3.14,
        "title": "ajax and jinja",
        "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
        + "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
        + " when an unknown printer took a galley of type and scrambled it to make a type specimen book. !@#",
        "float1": 3.14,
        "menu": ["home", "about", "contact"],
    }
    return render(request, "filters_jinja_django.html", context)


@login_required
def home(request):
    context = {
        "menu": MENU,
        "title": "Главная",
        "j": [1, 2, 3, 4, 5, 6, 7],
        "hosts": HostItem.objects.all(),
    }
    return render(request, "home.html", context)


@login_required
def detail(request, id):
    images = HostItemImages.objects.filter(host_item_id=id)
    user = UserProfile.objects.get(user_id=request.user.id)
    if request.method == "POST":
        if "rewiew" in request.POST:
            rewiew = str(request.POST.get("review"))
            rating = int(request.POST.get("rating"))
            alredy_feedback = Feedback.objects.filter(
                user_id=request.user.id, host_id=id
            )
            feedback = Feedback(
                message=rewiew, rating=rating, host_id=id, user_id=request.user.id
            )
            if not alredy_feedback:
                feedback.save()

        if "connect" in request.POST:
            host = HostItem.objects.get(id=id)
            chat = Chats.objects.get_or_create(
                receiver_id=request.user.id,
                host_id=host.user.id,
                hoster_id=host.user.id,
            )
            return redirect("chats")
    feedbacks = Feedback.objects.filter(host_id=id)
    middle_rating = 0
    for feedback in feedbacks:
        middle_rating += feedback.rating
    if feedbacks:
        middle_rating = middle_rating / len(feedbacks)

    context = {
        "menu": MENU,
        "title": "Подробнее",
        "host": HostItem.objects.get(id=id),
        "images": images[1:],
        "first_image": images[0].image.url,
        "user": user,
        "rewiews": Feedback.objects.filter(host_id=id),
        "rewiew_form": RewiewForm(),
        "middle_rating": middle_rating,
    }
    return render(request, "detail-host.html", context)


@login_required
def profile(request):
    profile_user = UserProfile.objects.get(user_id=request.user.id)
    if request.method == "POST":
        if "host-form" not in request.POST:
            form = UserProfileForm(request.POST, request.FILES)
            if form.is_valid():
                user = User.objects.get(id=request.user.id)
                user.first_name = form.cleaned_data["first_name"]
                user.last_name = form.cleaned_data["last_name"]
                user.email = form.cleaned_data["email"]
                user.username = form.cleaned_data["username"]
                if form.cleaned_data["description"]:
                    user_profile = UserProfile.objects.get(user_id=request.user.id)
                    user_profile.description = form.cleaned_data["description"]
                    user_profile.save()
                user.save()
                request.user = user
                if form.cleaned_data["image"]:
                    try:
                        file_path = rename_image(
                            form.cleaned_data["image"], request.user.id
                        )
                        profile_user.image = file_path
                        profile_user.save()
                    except FileExistsError:
                        pass
        else:
            form = UserHostForm(request.POST, request.FILES)
            if form.is_valid():
                file_path = rename_image_host(
                    form.cleaned_data["image"], request.user.id
                )
                host_item = HostItem(
                    user_id=request.user.id,
                    name=form.cleaned_data["name"],
                    price=form.cleaned_data["price"],
                    discount=form.cleaned_data["discount"],
                    description=form.cleaned_data["description"],
                    image=file_path,
                )
                host_item.save()

                for file in request.FILES.getlist("file_field"):
                    file_path = rename_images_host(file, request.user.id)
                    HostItemImages.objects.create(
                        host_item_id=host_item.id, image=file_path
                    )
    user = User.objects.get(id=request.user.id)
    profile_user = UserProfile.objects.get(user_id=request.user.id)
    user_hosts = HostItem.objects.filter(user_id=request.user.id)
    context = {
        "menu": MENU,
        "profile_form": UserProfileForm,
        "title": "Профиль",
        "user": user,
        "profile_user": profile_user,
        "service_form": UserHostForm,
        "hosts": user_hosts,
    }
    return render(request, "profile.html", context)


@login_required
def edit_host(request, id):
    host = HostItem.objects.get(id=id)
    if request.method == "POST":
        form = UserHostEditForm(request.POST, request.FILES)
        if form.is_valid():
            host.name = form.cleaned_data["name"]
            host.price = form.cleaned_data["price"]
            host.discount = form.cleaned_data["discount"]
            host.description = form.cleaned_data["description"]
            if form.cleaned_data["image"]:
                file_path = rename_image_host(
                    form.cleaned_data["image"], request.user.id
                )
                host.image = file_path
            host.save()
            return redirect("profile")
    context = {
        "host": host,
        "menu": MENU,
        "title": "Редактирование",
        "service_form": UserHostEditForm,
    }
    return render(request, "edit_host.html", context)


@login_required
def chats(request):
    user = UserProfile.objects.get(user_id=request.user.id)
    chats_receiver = Chats.objects.filter(receiver_id=user)
    chats_hoster = Chats.objects.filter(hoster_id=user)
    chats = chats_receiver.union(chats_hoster)
    context = {
        "menu": MENU,
        "appears": chats,
        "user": user,
        "title": "Чат",
    }
    return render(request, "chats.html", context)


@login_required
def chat(request, id):
    user = UserProfile.objects.get(user_id=request.user.id)
    chat = Chats.objects.get(id=id)
    if chat.hoster != user.id and chat.receiver != user:
        return redirect("chats")
    messages = Message.objects.filter(chat_id=chat)
    if request.method == "POST":
        message = Message(
            user_id=user.id,
            chat_id=chat.id,
            message=str(request.POST["message"]),
        )
        message.save()
    context = {
        "menu": MENU,
        "messages": messages,
        "title": "Чат",
        "chat": chat,
        "user": user,
    }
    return render(request, "chat.html", context)
