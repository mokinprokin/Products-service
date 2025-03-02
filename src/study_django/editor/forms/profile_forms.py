from editor.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserProfileForm(forms.Form):
    first_name = forms.CharField(max_length=18, label="Имя")
    last_name = forms.CharField(max_length=18, label="Фамилия")
    email = forms.EmailField(label="Email")
    username = forms.CharField(max_length=18, label="Имя пользователя")
    description = forms.CharField(
        max_length=1800,
        label="Описание профиля",
        required=False,
        widget=forms.Textarea(),
    )
    image = forms.ImageField(label="Изображение", required=False)


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserHostForm(forms.Form):
    name = forms.CharField(max_length=30, label="Название услуги", required=True)
    price = forms.IntegerField(label="Цена услуги", required=True)
    discount = forms.IntegerField(
        label="Скидка", required=True, max_value=99, min_value=0
    )
    image = forms.ImageField(label="Изображение на главном экране", required=True)
    description = forms.CharField(
        label="Описание услуги", required=True, widget=forms.Textarea()
    )
    file_field = forms.ImageField(
        label="Дополнительные изображения",
        required=True,
        widget=forms.ClearableFileInput(),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add the `multiple` attribute to allow selecting multiple files
        self.fields["file_field"].widget.attrs.update({"multiple": "true"})
class UserHostEditForm(forms.Form):
    name = forms.CharField(max_length=30, label="Название услуги", required=True)
    price = forms.IntegerField(label="Цена услуги", required=True)
    discount = forms.IntegerField(
        label="Скидка", required=True, max_value=99, min_value=0
    )
    image = forms.ImageField(label="Изображение на главном экране", required=False)
    description = forms.CharField(
        label="Описание услуги", required=True, widget=forms.Textarea()
    )