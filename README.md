# AdsApi(тестовое задание)
## Описание
API-сервис для получения данных об объявлениях.
## Технологии:
* Python
* Django
* Drf
* Jwt

## Запуcк из Docker 
Запуск производился на windows10(git)
### Клонирование
Клонируйте репозиторий
```
git clone git@github.com:V0yager01/AdsApi.git
```
### Запуск Docker compose 
В директории запускаем docker-compose.yml
```
docker compose up -d
```
### Подготовка Django
Выполняeм миграцию
```
docker compose exec adsapi python manage.py migrate
```
Загружаем данные из csv файла в бд
```
docker compose exec adsapi python manage.py load_ads
```
## Обычный запуск
### Клонирование
Клонируйте репозиторий
```
git clone git@github.com:V0yager01/AdsApi.git
```
### Подготовка виртуального окружения
Создаем и включаем окружение для проекта
```
python -m venv venv
source venv/Scripts/activate
```
### Установка зависимостей
```
cd adapi/
pip install -r requirements.txt
```
### Подготовка Django
Выполняeм миграцию
```
python manage.py migrate
```
Загружаем данные из csv файла в бд
```
python manage.py load_ads
```
### Запуск
```
python manage.py runserver
```
## Запросы 
### Создание пользователя
На эндопоинт отправляем имя и пароль 
```
POST /api/v1/user/
{
    "username": "username",
    "password": "password"
}
```
### Получение "access" jwt-токена
```
POST /api/v1/auth/token/
{
    "username": "username",
    "password": "password"
}
```
### Получение объявлений. 
Указываем в заголовке полученный "access" токен.

```
Authorization: Bearer "token"

GET /api/v1/ads/

GET /api/v1/ads/{id}

```

## Автор
Халиуллин Ильяс
