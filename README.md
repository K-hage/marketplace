[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Торговая площадка)](https://git.io/typing-svg)

### Требования:

- python 3.10
- docker

### 1. Как запустить проект:

---

Переходим в папку market_postgres.

``` shell
cd market_postgres
```

Выполняем команду

``` shell
docker-compose up --build -d
```

Frontend-часть проекта будет доступна по адресу

[http://localhost:3000](http://localhost:3000)

Backend-часть проекта будет доступна по ссылке:

[Swagger](http://localhost:8000/api/schema/swagger-ui/)
___

### 2. Как остановить и очистить проект:

В папке market_postgres в терминале прописать:

``` shell
docker-compose down
```

Бэкенд-часть проекта реализует следующий функционал:
---

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту.
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.





