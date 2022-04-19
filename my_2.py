"""9. Дано рядок, що містить принаймні один символ пробілу. Вивести підстроку,
розташовану між першим і останнім пробілом  початкового рядка. Якщо рядок  містить
тільки один пробіл, то вивести порожній рядок."""


def sub_string(string: str) -> str:
    counts = string.count(' ')
    if counts == 1:
        return ' '
    elif counts == 0:
        return 'В строке нет пробелов!'
    else:
        first = string.find(' ')
        last = string.rfind(' ')
        return string[first:last].strip()


def main():
    print(" Добро пожаловать в программу нахождения подстроки между двумя пробелами!")
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
            print(sub_string(s))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
