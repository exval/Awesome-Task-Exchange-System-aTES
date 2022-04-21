# Awesome-Task-Exchange-System-aTES


## Services:

+ Task-manager.
+ Auth.
+ Accounting/analytics.
+ DB.

---
## Task-manager.
Основная задача сервиса - выстроить логику работу юзеров с тасками. Сервис хендлит логику ассайнов.  

## Auth.
Проверяет наличие юзеров, идентифицирует их контролит их роли. Сервис хендлит логику ролей.

## Accounting/analytics.
Считает и анализирует кто сколько заработал и проч. 

## DB.
Хранит и отдает данные (:

---

## Architecture as pic.
![awesomeTaskManager!](imgs/awesomeTaskManager.jpeg "awesomeTaskManager")

---

## How to resolve:
+ Падение сети.
Иметь резервную сеть :)
+ Падение базы данных.
Настроить репликацию, сделать ручку для переключения баз данных master -> slave. 

## Problems:
+ Думаю, что можно добавить кафку и вынести accounting/analytics как асихронные сервисы: ходить в кафку, забирать оттуда данные на основе этого отдавать необходимую дату. 
+ Нелокальная БД возможно будет замедлять работу сервиса.
+ На данный момент сервис полностью синхронный. 
