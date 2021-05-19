# E-7.11

## Описание

Приложение на Flask: 
	* flask-mongoengine
	* flask-restful
	* flask-caching
    * GET-запросы кэшируются в Redis

### Инсталяция:

-> скачать приложение
-> собрать контейнеры $ docker-compose build
-> запуск контейнеров $ docker-compose up

#### Пользование:

-> статистика объявления
/stat GET

-> получить все объявления
/advs GET

-> добавить новое объявление 
/advs POST

-> получить объявление по идентификатору
/adv GET

-> поменять поле объявления
/adv PATCH
title="New Title"

-> удалить объявление
/adv DELETE

-> добавить тэг в объявлении
/tags POST

-> удалить тэг в объявлении
/tags DELETE

-> добавить комментарий в объявлении
/comment POST