""" 10. Дано рядки S, S1 і S2. Замінити в рядку S остання входження рядка S1 на рядок S2."""


def string_change(string: str, string_1: str, string_2: str) -> str:
    counts = string.count(string_1)
    if counts == 0:
        return f'В строке не найдено подстроку {string_1}'
    else:
        previous, old, next = string.rpartition(string_1)
    return previous + string_2 + next


def main():
    print(" Добро пожаловать в программу изменения последнего вхождения подстроки на другую строку!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Преобразить строку
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    s = input("Введите строку (не пустую!) ")
                    if s == "":
                        print("Строка не должна быть пустой!")
                    else:
                        break
                except ValueError:
                    print("Несоответствие типов!")
            while True:
                try:
                    s_1 = input("Введите подстроку (не пустую!) ")
                    if s_1 == "":
                        print("Строка не должна быть пустой!")
                    else:
                        break
                except ValueError:
                    print("Несоответствие типов!")
            while True:
                try:
                    s_2 = input("Введите строку, которой хотите заменить подстроку (не пустую!) ")
                    if s_2 == "":
                        print("Строка не должна быть пустой!")
                    else:
                        break
                except ValueError:
                    print("Несоответствие типов!")
            print(string_change(s, s_1, s_2))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
