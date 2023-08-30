### Пет-проект по созданию интренет магазина програмного обеспечения" .

### Цель: Создать в команде интеренет приложения на Python используя веб-фреймворк Django.

### Комманда учеников:
- Федор Санников (https://github.com/FedorSannikov1988; fedor.sannikov88@gmail.com) - фулстек-разработчик;
- Артем Федотов (https://github.com/fedotoff144; fedotoff144@gmail.com) - фулстек-разработчик;
- Михаил Зиновьев (https://github.com/ZinovevMY; mehan@list.ru) - фулстек-разработчик;
- Анатолий Ступин (https://github.com/Trotil2001; trotil_2001@mail.ru) - фулстек-разработчик;

### Технологии и инструменты:
 - Веб-фреймворк: Django версии 3.2;
 - Язык программирования Python версии 3.10; 
 - СУБД: SQLite (на начальном этапе), PostgreSQL (на завершающем этапе); 
 - Язык гипертекстовой разметки: HTML совместно с каскадными таблицами стилей CSS;

### Порядок загрузки фикстур (shop/fixtures) в проект:

1. SoftwareCategory.json
2. Software.json
3. FeaturesSoftware.json
4. DevelopmentTeam.json
5. FAQ.json
6. User.json
7. UsersQuestions.json
8. ImageCollectionForIndex.json

### Команда для загрузки фикстуры:
python manage.py loaddata shop/fixtures/<имя фикстуры>

### Актуальные медиафайлы (папка media):
https://disk.yandex.ru/d/IPC8WI9Xg12TUA

### Архив с файлом .env:
https://disk.yandex.ru/d/eY5sc6zQECOwSw

##### Внимание:
##### Архив с файлом .env защищен паролем.
##### Пароль можно получить у команды разработки проекта.

### Создание базы даных PostgreSQL:
1. CREATE DATABASE shop_db;
2. CREATE ROLE admin with password "введите пароль из файла .env переменная db_password";
3. ALTER ROLE "admin" WITH LOGIN;
4. GRANT ALL PRIVILEGES ON DATABASE "shop_db" to admin;
5. ALTER USER admin CREATEDB;
