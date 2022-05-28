# Awesome-Task-Exchange-System-aTES

## Description
Task tracker for parrots.

## Installation
1. Clone repo.
```
https://github.com/exval/Awesome-Task-Exchange-System-aTES.git
```
2. Move to project directory.
```
cd awesome_task_manager/project
```
3. Build the project
```
docker-compose up -d --build
```
4. Create superuser 
```
docker-compose exec auth src/manage.py createsuperuser
```
5. Collect static:
```
docker-compose exec auth src/manage.py collectstatic
```
6. Go to `http://127.0.0.1:8000/o/applications` and register new application:
- client type: `confidential`
- Authorization grant type: `Resource owner password-based`
- Copy `cliend_id`/`client_secret` and paste into taskmanager settings.

7. Setup taskmanager:
```
docker-compose exec taskmanager src/manager.py makemigrations
docker-compose exec taskmanager src/manager.py migrate
docker-compose exec taskmanager src/manager.py collectstatic
docker-compose exec taskmanager src/manager.py run_consumer
```

## Project's events.
![Events!](imgs/projects_events.png "Events")

## Data modeling and domains.
![Data model!](imgs/data_model.png "Data model")

## Architecture scheme
![Architecture!](imgs/Architecture.png "Architecture in scheme")

## TODO:
- Make more complete desctiption.


