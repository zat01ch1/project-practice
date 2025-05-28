# Отчет: Разработка сайта музыкальных рецензий на Hugo

## Шаг 1: Инициализация проекта
```bash
hugo new site music-reviews
cd music-reviews
```
## Шаг 2: Добавление темы Ananke
```bash
git init
git submodule add https://github.com/theNewDynamic/gohugo-theme-ananke.git themes/ananke
echo 'theme = "ananke"' >> config.toml
```
## Шаг 3: Создание структуры контента
```bash
hugo new _index.md
hugo new about.md
hugo new team.md
hugo new resources.md
hugo new posts/first-review.md
```
## Шаг 4: Наполнение главной страницы (content/_index.md)
```bash
---
title: "MUSICWORLD"
date: 2024-05-20
---
## Лучшие музыкальные рецензии
- Новые релизы
- Экспертные оценки
- Интервью с артистами
```
##Шаг 5: Создание рецензии
```bash
---
title: "PHARAOH - 10:13"
date: 2024-04-25
draft: false

rating: 9/10
---

![Обложка альбома 10:13](/images/PH.jpg)  
*Обложка альбома "10:13" --- "в одной руке лилия, в другой ствол - Архангел Гавриил"*
```
##Шаг 8: Запуск локального сервера
```bash
hugo server -D
```
##Итоговая функциональность
Структура сайта:
Главная страница
Раздел "О проекте"
Страница команды
Блог с рецензиями
Особенности:
Адаптивный дизайн
Поддержка Markdown
Быстрая загрузка
Технологии:
Hugo (генератор статических сайтов)
Git (контроль версий)
