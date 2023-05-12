# Notification_service

## Шаг 1:

Запустите команду
```sh
git clone git@github.com:Sniperat/Notification_service.git && cd Notification_service/
```
## Шаг 2:
Создайте файл <i><b>`.env`</b></i> в директории <b>`config/`</b> и внесите следующие данные:

[//]: # (Create a file named   <i><b>`.env`</b></i>   inside of <b>`config/`</b> package and fill it with the following information:)

```
SECRET_KEY=
DEBUG=True
REDIS_HOST=127.0.0.1
REDIS_PORT=6379
TOKEN=  //токен для пробного сервера
DATABASE_NAME=postgres
DATABASE_USER=postgres
DATABASE_PASS=postgres
DATABASE_HOST=db
DATABASE_PORT=5432
CELERY_BROKER=redis://redis:6379/0
CELERY_BACKEND=redis://redis:6379/0
// адрес эл. почты для получения дневной статистики;
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```
## Шаг 3:
Убедитесь что на вашем устройстве установлен Docker;

Запустите следующую команду на терминале;

```sh
docker-compose up -d --build
```
После запуска на вашем [localhost:8000](http://localhost:8000/) будет запущен проект

[//]: # (After that on your [localhost]&#40;http://localhost:8000/&#41; running that web application with port `8000` )
По адресу [localhost:8000/docs](http://localhost:8000/docs) доступна документация к api

По адресу [localhost:8000/admin](http://127.0.0.1:8000/admin/) доступна панель администрирования ,
но для входа сначала нужно создать пользователя запустив в терминале эту команду


```sh
docker-compose exec web python manage.py createsuperuser
```

Следующая команда нужна для отключения программы 
```sh
docker-compose down
```
### Список выполненных дополнительных заданий:
    1. подготовить docker-compose для запуска всех сервисов проекта одной командой
    2. сделать так, чтобы по адресу /docs/ открывалась страница со Swagger UI и в 
    нём отображалось описание разработанного API. Пример: https://petstore.swagger.io
    3. реализовать администраторский Web UI для управления рассылками и получения статистики по отправленным сообщениям
    4. реализовать дополнительный сервис, который раз в сутки отправляет статистику по обработанным рассылкам на email
    5. удаленный сервис может быть недоступен, долго отвечать на запросы или выдавать некорректные ответы. 
    Необходимо организовать обработку ошибок и откладывание запросов при неуспехе для последующей повторной отправки. 
    Задержки в работе внешнего сервиса никак не должны оказывать влияние на работу сервиса рассылок.
#### Спасибо
для вопросов `+998995047024` or [telegram](https://t.me/just_akbarov)