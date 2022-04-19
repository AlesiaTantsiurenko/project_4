""" 14. Дано два упорядкованих за спаданням списки. Об'єднайте їх в новий упорядкований за спаданням
список."""


def lists(s_1: str, s_2: str) -> list:
    lst1 = [int(i) for i in s_1.split()]
    lst2 = [int(i) for i in s_2.split()]
    lst1.sort(reverse=True)
    lst2.sort(reverse=True)
    lst3 = lst1 + lst2
    lst3.sort(reverse=True)
    return lst3


def main():
    print(" Добро пожаловать в программу сортировки списков!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Объединить отсортированные списки в один отсортированый список
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    string_1 = input("Введите первый список целых чисел ")
                    if string_1 != "" and string_1.replace(" ", "").isdigit():
                        break
                    else:
                        print("Строка должна состоять из целых цифр!")
                except ValueError:
                    print("Несоответствие типов!")
            while True:
                try:
                    string_2 = input("Введите второй список целых чисел ")
                    if string_2 != "" and string_2.replace(" ", "").isdigit():
                        break
                    else:
                        print("Строка должна состоять из целых цифр!")
                except ValueError:
                    print("Несоответствие типов!")
            print(lists(string_1, string_2))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
