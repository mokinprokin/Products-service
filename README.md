# 🏠 RentHub — маркетплейс объявлений с мессенджером

**Аналог Avito с удобными чатами и системой отзывов**

![Project Banner](https://via.placeholder.com/800x300?text=RentHub+Marketplace)

---

## ✨ Особенности проекта

| 🛡️ Безопасность         | 💬 Общение               | 📊 Аналитика            |
|------------------------|-------------------------|------------------------|
| Регистрация и вход     | Чат между пользователями | Рейтинги и отзывы      |
| Личный кабинет         | Быстрые сообщения        | История сделок         |

---

## 🚀 Функционал

### 🔐 Аутентификация и профиль
- 📝 Регистрация / вход через email
- 🖼️ Загрузка аватарки
- ✏️ Редактирование профиля
- 📍 Контактные данные

### 🏡 Система объявлений
- Создание и редактирование объявлений
- Загрузка нескольких фотографий
- Указание цены и скидки
- Детальное описание товаров

### 💬 Встроенный мессенджер
- 🔔 Уведомления о новых сообщениях
- 📅 История переписки
- 🚀 Быстрые ответы

### ⭐ Система отзывов
- Оценка качества сделки
- Текстовые отзывы
- Средний рейтинг пользователя

---

## 🛠 Технологии

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)
![Django](https://img.shields.io/badge/Django-4.0-green?logo=django)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13-blue?logo=postgresql)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap)

---

## ⚙️ Установка

```bash
# 1. Клонировать репозиторий
git clone https://github.com/yourusername/RentHub.git
cd RentHub

# 2. Установить зависимости
pip install -r requirements.txt

# 3. Применить миграции
python manage.py migrate

# 4. Создать админа
python manage.py createsuperuser

# 5. Запустить сервер
python manage.py runserver
