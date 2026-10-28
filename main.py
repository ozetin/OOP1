from zadaniya.zadanie_1 import sozdat_zamikanie, umnozhit
from zadaniya.zadanie_2 import Poezd


def zadanie_1():
    print("\nЗадание 1")

    a = int(input("Введите a: "))
    b = int(input("Введите b: "))

    func = sozdat_zamikanie(umnozhit)

    print(func(a, b))


def vvod_poezdov():
    poezda = []

    kol = int(input("Введите количество поездов: "))

    for i in range(kol):
        print(f"\nПоезд {i + 1}")

        kuda = input("Введите пункт назначения: ")
        number = int(input("Введите номер поезда: "))
        time = input("Введите время отправления: ")

        poezd = Poezd(kuda, number, time)
        poezda.append(poezd.get_slovar())

    return poezda


def sortirovka(spisok):
    return sorted(spisok, key=lambda x: x["number"])


def vyvod_spiska(spisok):
    print("\nСписок поездов:")

    for poezd in spisok:
        print(
            f'Номер: {poezd["number"]}, '
            f'пункт назначения: {poezd["punkt"]}, '
            f'время отправления: {poezd["time"]}'
        )


def poisk_poezda(spisok):
    number = int(input("\nВведите номер искомого поезда: "))
    naydennye = []

    for poezd in spisok:
        if poezd["number"] == number:
            naydennye.append(poezd)

    if len(naydennye) == 0:
        print("Поезд с таким номером не найден")
    else:
        for poezd in naydennye:
            print(
                f'Пункт назначения: {poezd["punkt"]}\n'
                f'Номер поезда: {poezd["number"]}\n'
                f'Время отправления: {poezd["time"]}'
            )


def zadanie_2():
    print("\nЗадание 2")

    spisok = vvod_poezdov()
    spisok = sortirovka(spisok)

    vyvod_spiska(spisok)
    poisk_poezda(spisok)

if __name__ == "__main__":
    zadanie_1()
    zadanie_2()