import database


# Пример использования
if __name__ == "__main__":
    db = database.HabitTrackerDatabase("habit_tracker.db")

    # Добавление новых пользователей в БД - добавил
    # db.add_user(5185362611, "Эдуард")
    # db.add_user(258128224, "Денис")
    # db.add_user(949247259, "Юрий")
    # db.add_user(1328953283, "Лев")
    # db.add_user(388383693, "Татьяна")

    # Добавление новых привычек в БД
    # db.add_habit(1, "Правильное питание", "Есть овощи 3 раза в день", 3,
    #              "07:00", "19:00")
    # db.add_habit(1, "Водопой", "Пить воду 6 раз в день", 6,
    #              "07:00", "19:00")
    # db.add_habit(1, "Спорт", "Заниматься спортом 1 раз в день", 1,
    #              "18:00", "22:00")

    db.add_habit(2, "Утренняя зарядка", "Делать зарядку по утрам", 1,
                 "06:00", "06:30")
    db.add_habit(2, "Чтение книг", "Читать книги каждый день по 30 минут", 1,
                 "20:00", "20:30")
    db.add_habit(2, "Пить воду", "Пить 8 стаканов воды в день", 8,
                 "08:00", "22:00")

    db.add_habit(3, "Медитация", "Медитировать по утрам", 1,
                 "07:30", "08:00")
    db.add_habit(3, "Изучение иностранного языка", "Изучать английский язык 1 час каждый день",
                 1, "18:00", "19:00")
    db.add_habit(3, "Беговые тренировки", "Бегать 4 раза в день", 4,
                 "06:00", "18:00")

    db.close_connection()
