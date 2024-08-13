# api_final
Финальная версия API для сервиса YaTube.

### Как запустить проект:
Клонировать репозиторий через терминал:

```
git clone https://github.com/wiacze/api_final_yatube.git
```

Создать и активированить виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
```

Или:

```
python -m venv venv
source venv/Scripts/activate
```

Обновить pip:

```
python3 -m pip install --upgrade pip
```

Или:


```
python -m pip install --upgrade pip
```

Установить все зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в директорию с файлом manage.py и выполнить миграции:

```
python3 manage.py migrate
```

Или:

```
python manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Или:

```
python manage.py runserver
```
