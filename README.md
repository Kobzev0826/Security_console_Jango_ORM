# Пульт охраны 
программа с использованием фреймворка Jango.\
При переходе по адресу развертывания данной программы позволяет увидеть:
- список всех активных карт доступа `/`
- список пользователей в хранилище `/storage_information`
- список всех визитов по выбранному пользователю `/passcard_info/<passcard_id>`

## Необходимо для запуска\развертывания
- python3
- Jango
- подключение к базе данных (БД)
### Как настроить подключение к БД 
создать переменные окружения в файле `.env`
- хост `DB_HOST`
- порт `DB_PORT`
- имя БД `DB_NAME`
- имя пользователя `DB_USER`
- пароль `DB_PASSWORD`
### Что есть еще ?
переменные окружения:
`DEBUG` - `default = false` булевая переменная позволяет включать или отключать отладочный режим,
`DB_SECRET_KEY` - Secret key

# Как установить
Python3 должен быть уже установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
