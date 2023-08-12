### Дипломный проект:

### Идея: "Учебный проект по созданию интренет магазина програмного обеспечения" .

### Цель: "Научиться создавать интеренет приложения/сайты на Python используя веб-фреймворк Django в комманде." .

### Комманда учеников:
- Федор Санников (fedor.sannikov88@gmail.com) - фулстек-разработчик, менеджер проекта 
- Артем Федотов (fedotoff144@gmail.com) - фулстек-разработчик 
- Михаил Зиновьев (mehan@list.ru) - фулстек-разработчик 
- Анатолий Ступин (trotil_2001@mail.ru) - фулстек-разработчик

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
https://disk.yandex.ru/d/LHKe-C0lMaZNsA

### Файлы с паролями о проекта db.password, django.key, email.password:
https://disk.yandex.ru/d/hz2HxRLMnIrqKw

##### Внимание: Архив с файлами: db.password, django.key, email.password запаролен.
##### Пароль можно получить у команды разработки проекта.

### Создание базы даных PostgreSQL:
1. CREATE DATABASE shop_db;
2. CREATE ROLE admin with password "введите пароль из файла db.password";
3. ALTER ROLE "admin" WITH LOGIN;
4. GRANT ALL PRIVILEGES ON DATABASE "shop_db" to admin;
5. ALTER USER admin CREATEDB;
