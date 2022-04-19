""" 4. Дано не порожній рядок S. Вивести рядок, що  містить символи рядка S,
між якими встановлено по одному пробілу. """


def string_change(string: str) -> str:
    return ' '.join(string.replace(' ', ''))


def main():
    print(" Добро пожаловать в программу перевоплощения строки!")
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
            print("Теперь наша строка розбита на символы: ", string_change(s))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
