## Описание 
Сборка курса валют со страницы https://www.cbr-xml-daily.ru/daily_json.js

## Стек технология:
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

## Запуск проекта 
```
git clone git@github.com:Ilnurr/kokos_project.git
```
Создать виртуальное окружение:

```
python3 -m venv env
```

Активировать виртуальное окружение:

```
source env/bin/activate 
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt 
```
 
Выполнить миграции:

```
python3 manage.py migrate 
```

Запустить проект:

```
python3 manage.py runserver
```
Импорт данных с json 
```
python3 manage.py import_data
```
