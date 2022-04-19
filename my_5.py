""" 19. Дано список. Виведіть ті його елементи, які зустрічаються в списку тільки один раз. Елементи
потрібно виводити в тому порядку, в якому вони зустрічаються в списку."""


def sort_list(s: str, lst: list) -> str:
    lst_2 = []
    for a in s.split():
        if a in ["True", "False"]:
            lst.append(bool(a))
        elif a.isdigit():
            lst.append(int(a))
        elif a.replace('.', '', 1).isdigit():
            lst.append(float(a))
        else:
            lst.append(a)
    for i in lst:
        if lst.count(i) == 1:
            lst_2.append(i)
    return ', '.join(map(str, lst_2))


def main():
    list = []
    print(" Добро пожаловать в программу нахождения уникальных элементов списка!")
    choice = None
    while choice != "0":
        print(
            """
            0 - Выйти
            1 - Найти уникальные элементы списков
            """
        )
        choice = (input("Ваш выбор - "))
        print()
        if choice == "0":
            print("До свидания!")
        elif choice == "1":
            while True:
                try:
                    string = input("Введите список элементов ")
                    if string != "":
                        break
                    else:
                        print("Строка должна быть заполнена элементами!")
                except ValueError:
                    print("Несоответствие типов!")
            print("Вот уникальные элементы списка: ", sort_list(string, list))
        else:
            print("Извините, в меню нет пункта ", choice, ".")


main()
