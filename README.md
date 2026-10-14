<div align="center">

# 🐳 Лабораторная работа №2
## Коммуникация в многоконтейнерных системах

![Docker](https://img.shields.io/badge/Docker-29.8.0-2496ED?logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)
![RabbitMQ](https://img.shields.io/badge/RabbitMQ-3.13-FF6600?logo=rabbitmq&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-4169E1?logo=postgresql&logoColor=white)

**Дисциплина:** Непрерывное интегрирование и сборка программного обеспечения  
**Выполнил:** Рахимзода Абубакр, группа 13  
**Вариант:** 8  
**Год:** 2026

</div>

---

## 📋 О проекте

Репозиторий содержит решения **лабораторной работы №2** по дисциплине «Непрерывное интегрирование и сборка программного обеспечения» (ФПМИ БГУ, кафедра ТП).

**Тема:** Коммуникация в многоконтейнерных системах.

В работе рассмотрены:
- 🔗 **Синхронная коммуникация** через bind mounts (Задание 1)
- 📨 **Асинхронная коммуникация** через брокер сообщений RabbitMQ (Упражнение 2.2)

---

## ✅ Выполненные задания

| № | Задание | Статус |
|:---:|---|:---:|
| **1** | Разработка простейшего распределённого приложения (вариант 8) | ✅ |
| **2.2** | RabbitMQ в Docker + уроки 1–3 на Python | ✅ |

> 📌 Для группы 13 (согласно методичке) обязательны **Задание 1** и **Упражнение 2.2**, а также ответы на 30 контрольных вопросов.

---

## 🗂️ Структура репозитория

---

# 🐳 Задание 1. Распределённое приложение

## 📝 Постановка задачи (вариант 8)

> **Программа 1** ищет в каталоге `/var/data` **самый большой по объёму файл** и копирует его в `/var/result/data.txt`.
>
> **Программа 2** ищет **наименьшее число** из файла `/var/data/data.txt` (результат работы Программы 1) и сохраняет **количество таких чисел** в `/var/result/result.txt`.

Связь между приложениями — через **bind mounts** (связанные тома).

## 🔗 Схема монтирования

| Программа | Хост-каталог | → | Контейнер | Режим |
|---|---|:---:|---|---|
| **worker1** | `./data` | → | `/var/data` | `ro` |
| **worker1** | `./result-1` | → | `/var/result` | `rw` |
| **worker2** | `./result-1` | → | `/var/data` | `ro` |
| **worker2** | `./result` | → | `/var/result` | `rw` |

💡 Каталог `./result-1` монтируется в **оба** контейнера: worker1 пишет туда, worker2 читает оттуда.

## ⚙️ `compose.yaml`

```yaml
services:
  worker1:
    build: ./worker1
    container_name: worker1
    volumes:
      - ./data:/var/data:ro
      - ./result-1:/var/result

  worker2:
    build: ./worker2
    container_name: worker2
    volumes:
      - ./result-1:/var/data:ro
      - ./result:/var/result
    depends_on:
      worker1:
        condition: service_completed_successfully
