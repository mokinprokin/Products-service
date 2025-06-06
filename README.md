# 🏠 RentHub — маркетплейс объявлений с мессенджером  

**Аналог Avito с удобными чатами и системой отзывов**  

![Project Banner](https://via.placeholder.com/800x300?text=RentHub+Marketplace)  
*(Замените на реальное изображение вашего проекта)*

---

## ✨ Особенности проекта

<div align="center">
  
| 🛡️ Безопасность | 💬 Общение | 📊 Аналитика |
|----------------|-----------|-------------|
| Регистрация и вход | Чат между пользователями | Рейтинги и отзывы |
| Личный кабинет | Быстрые сообщения | История сделок |

</div>

---

## 🚀 Функционал

### 🔐 Аутентификация и профиль
- 📝 Регистрация / вход через email
- 🖼️ Загрузка аватарки
- ✏️ Редактирование профиля
- 📍 Контактные данные

### 🏡 Система объявлений
```mermaid
graph TD
    A[Создание объявления] --> B[Фотографии]
    B --> C[Цена и описание]
    C --> D[Публикация]
    D --> E[Просмотры]
💬 Встроенный мессенджер
🔔 Уведомления о новых сообщениях

📅 История переписки

🚀 Быстрые ответы

🛠 Технологии
<div align="center">
https://img.shields.io/badge/Python-3.9+-blue?logo=python
https://img.shields.io/badge/Django-4.0-green?logo=django
https://img.shields.io/badge/PostgreSQL-13-blue?logo=postgresql
https://img.shields.io/badge/Bootstrap-5-purple?logo=bootstrap

</div>
⚙️ Установка
bash
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
Открыть в браузере: http://localhost:8000

📌 Дорожная карта
Базовая система объявлений

Мессенджер

Система уведомлений

Мобильное приложение

Платежная система

📜 Лицензия
Этот проект распространяется под лицензией MIT. Подробнее см. в LICENSE.
