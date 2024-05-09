### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/LolDen15/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```



### Примеры API:

Для получения списка всех постов пользователей:

```
http://127.0.0.1:8000/api/v1/posts/
```

Для получения отдельного поста

```
http://127.0.0.1:8000/api/v1/posts/{номер_поста}/
```

Подробную документацию API можно посмотреть на этом эндпоинте:
```
http://127.0.0.1:8000/redoc/
```