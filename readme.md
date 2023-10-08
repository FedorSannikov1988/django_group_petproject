### Пет-проект по созданию интренет магазина програмного обеспечения испоьзуя веб-фреймворк Django.

### Цель:

#### Создать в команде интеренет приложения на Python используя веб-фреймворк Django.

#### Эскиз всех воплощенных (работающих) страниц магазина: <a href="https://disk.yandex.ru/i/7U8C6LnwFQFshQ">эскиз</a>

### Комманда учеников:
- Федор Санников (<a href="https://github.com/FedorSannikov1988">GitHub</a>, email: fedor.sannikov88@gmail.com) - фулстек-разработчик;
- Артем Федотов (<a href="https://github.com/fedotoff144">GitHub</a>, email: fedotoff144@gmail.com) - фулстек-разработчик;
- Михаил Зиновьев (<a href="https://github.com/ZinovevMY">GitHub</a>, email: mehan@list.ru) - фулстек-разработчик;
- Анатолий Ступин (<a href="https://github.com/Trotil2001">GitHub</a>, email: trotil_2001@mail.ru) - фулстек-разработчик;

### Технологии и инструменты:
 - Веб-фреймворк: Django версии 3.2;
 - Язык программирования Python версии 3.10; 
 - СУБД: SQLite (на начальном этапе), PostgreSQL (на завершающем этапе); 
 - Язык гипертекстовой разметки: HTML совместно с каскадными таблицами стилей CSS;

## Запуск:

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

### Актуальные медиафайлы (папка media): <a href="https://disk.yandex.ru/d/IPC8WI9Xg12TUA">media</a>
Данные картинки необходимы для адекватного отображения проекта.

### Архив с файлом .env: <a href="https://disk.yandex.ru/d/eY5sc6zQECOwSw">.env </a>

В данном архиве находятся django key, пароль от электронной почты и пароль от базы данных 
(переменные: django_key, email_password и db_password соответственно).

##### Внимание:
##### Архив с файлом .env защищен паролем.
##### Пароль можно получить у команды разработки проекта.

### Создание базы даных PostgreSQL:
1. CREATE DATABASE shop_db;
2. CREATE ROLE admin with password "введите пароль из файла .env переменная db_password";
3. ALTER ROLE "admin" WITH LOGIN;
4. GRANT ALL PRIVILEGES ON DATABASE "shop_db" to admin;
5. ALTER USER admin CREATEDB;

<details><summary><strong>Структура базы данных (одна борльшая картинка):</strong></summary>

![database_structure](/pictures_for_readme/database_structure.png "database_structure") 

</details>

