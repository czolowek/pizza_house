import sqlite3


def create_db(name_db: str):
    try:
        sql_con = sqlite3.connect(name_db)
        cursor = sql_con.cursor()

        query = """
        CREATE TABLE IF NOT EXISTS Students (
        id INTEGER PRIMARY KEY,
        first_name VARCHAR(100),
        last_name TEXT,
        grade REAL
        );
        """
        print("Запит успішно сформовано")
        cursor.execute(query)
        sql_con.commit()
        print("Таблиця успішно створена")

    except sqlite3.Error as error:
        print("error: ", error)

    finally:
        cursor.close()
        sql_con.close()
        print("З'єднання з базою даних успішно завершене")


def add_student(first_name, last_name, grade):
    try:
        sql_con = sqlite3.connect("my_first.db")
        cursor = sql_con.cursor()

        query1 = f"""
        INSERT INTO Students (first_name, last_name, grade) VALUES ('Вася', 'Пупкін', 78);
        """

        query2 = f"""
        INSERT INTO Students (first_name, last_name, grade) VALUES ('{first_name}', '{last_name}', {grade});
        """

        query3 = """
        INSERT INTO Students (first_name, last_name, grade) VALUES (?, ?, ?)
        """

        cursor.execute(query3, (first_name, last_name, grade))
        sql_con.commit()
        print("Дані успішно записані")

    except sqlite3.Error as error:
        print("Помилка: ", error)

    finally:
        cursor.close()
        sql_con.close()
        print("Підключення успішно завершене")


def get_studens():
    try:
        sql_con = sqlite3.connect("my_first.db")
        cursor = sql_con.cursor()

        query = """
        SELECT * FROM Students;
        """

        students = cursor.execute(query).fetchall()
        print("students: ", students)

        for student in students:
            print("Учень: ", student)

    except sqlite3.Error as error:
        print("error: ", error)

    finally:
        cursor.close()
        sql_con.close()


create_db("my_first.db")



get_studens()
add_student("екрович", "Іванов", 96)
add_student("марк", "игоревич", 88)
add_student("игор", "кукушкин", 14)
add_student("маслан", "стандарт", 44)
add_student("григорич", "аркабич", 68)
add_student("Микола", "ктото", 67)