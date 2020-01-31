import random
import string


def search_number_symbol():
    """ Функция поиска номеров символов, совпадающих с последним символом строки """
    print('Введите строку')
    str = input()
    n = len(str)
    last_symbol = str[n - 1]
    list_number_symbol = []
    n -= 1
    for _ in range(n+1):
        if str[n] == last_symbol:
            list_number_symbol.append(n + 1)
        n -= 1
    print(list_number_symbol)


def search_first_last_middle_symbol():
    """ Функция поиска первого, последнего  и среднего(если он есть) символов """
    print('Введите строку')
    str = input()
    n = len(str)
    id_middle_symbol = int(n//2)
    middle_symbol = str[id_middle_symbol]
    if n % 2 == 0:
        print(str[0], str[n-1])
    else:
        print(str[0], middle_symbol, str[n-1])


def search_longest_word():
    """ Функция поиска самого длинного слова """
    print('Введите строку')
    str = input()
    str = str.split()
    n = len(str)
    id_longest_word = 0
    for i in range(n):
        if len(str[id_longest_word]) < len(str[i]):
            id_longest_word = i
    print(str[id_longest_word])


def three_different_symbol():
    """ Функция удаляет три любых символа если в строке больше трех
    различных символов, иначе добавить в строку в произвольных местах новые элементы так, чтобы
    количество различных элементов было больше трех."""
    print('Введите строку')
    str = input()
    # n = len(str)
    # quantity_different_symbol=1
    # i = 1
    # for i in range(n):
    #     if str[0] != str[i]:
    #         for k in range(i,n-1,1):
    #              if str[i]!=str[k]:
    #                  quantity_different_symbol += 1
    #              k+=1
    #                 i+=1
    print('quantity_different_symbol')


def search_word_from_numbers():
    """Дан текст. Найти слова, состоящие из цифр, и сумму чисел, которые образуют эти слова."""
    print('Введите текст')
    str = input()
    str = str.split()
    n = len(str)
    list_word_from_numbers = []
    sum_of_numbers = 0
    for i in range(n):
        if str[i].isdigit():
            list_word_from_numbers.append(str[i])
            sum_of_numbers += int(str[i])
    print(list_word_from_numbers, sum_of_numbers)


def search_word_separated_by_characters():
    """ Функция ищет слова разделенные заданными символами"""
    print('Введите строку')
    str = input()
    str_characters = ['!', '.', '/', '+', '>', '<']
    n = len(str)
    for i in range(n):
        if str[i] in str_characters:
            str = str.replace(str[i], ' ')
    str = str.split()
    print(str)


def defines_is_string_number():
    """ Функция определяет является ли строка действительным числом"""
    print('Введите строку')
    str = input()
    print('это действительное чиcло' if str.isdigit() else 'это не число')



def characters_based_length_str():
    """ Функция выводит первые три символа и последниe три символа,
     если длина строки больше 5. Иначе первый символ столько раз, какова длина строки."""
    print('Введите строку')
    str = input()
    n = len(str)
    str_from_first_symbol = []
    if n > 5:
        print(str[0], str[1], str[2], str[n - 3], str[n - 2], str[n - 1])
    else:
        for _ in range(n):
            str_from_first_symbol.append(str[0])
        print(str_from_first_symbol)


def forms_string_of_10_characters():
    """ Функция формирует строку из 10 символов.
    На четных позициях должны находится четные цифры, на нечетных позициях - буквы."""
    str = []
    for i in range(10):
        if i % 2 == 0:
            symbol = random.randint(0, 9)
        else:
            symbol = random.choice(string.ascii_letters)
        str.append(symbol)
    print(str)


def search_numbers_in_string():
    """ Функция ищет в строке количество цифр"""
    print('Введите строку')
    str = input()
    n = len(str)
    numbers_in_string = 0
    for i in range(n):
        if str[i] in "0123456789":
            numbers_in_string += 1
    print(numbers_in_string)


def string_matching():
    """ Функция определяет, можно ли из некоторых символов первой строки составить вторую строку."""
    print('Введите первую строку')
    str_first = input()
    print('Введите вторую строку')
    str_second = input()
    n = len(str_second)
    for i in range(n):
        if str_second[i] in str_first:
            str_first = str_first.replace(str_second[i], "")
        else:
            print('Из первой строки нельзя составить вторую')
            exit()
    print('Из первой строки можно составить вторую')


def change_word():
    """ Функция заменяет в строке все вхождения 'word' на 'letter'."""
    print('Введите первую строку')
    str = input()
    str = str.replace('word', 'letter')
    print(str)


def choice_number():
    print('Введите из нижеперечисленых номер задачи, выход "0"')
    task_number = ['3','7', '11', '15', '19', '23', '27', '31', '35', '43', '51', '59' ]
    print(task_number)
    task_number = int(input())
    if task_number == 3:
        print(search_number_symbol.__doc__)
        search_number_symbol()
    elif task_number == 7:
        print(search_first_last_middle_symbol.__doc__)
        search_first_last_middle_symbol()
    elif task_number == 11:
        print(search_longest_wordl.__doc__)
        search_longest_word()
    elif task_number == 15:
        print(three_different_symbol.__doc__)
        three_different_symbol()
    elif task_number == 19:
        print(search_word_from_numbers.__doc__)
        search_word_from_numbers()
    elif task_number == 23:
        print(search_word_separated_by_characters.__doc__)
        search_word_separated_by_characters()
    elif task_number == 27:
        print(defines_is_string_number.__doc__)
        defines_is_string_number()
    elif task_number == 31:
        print(characters_based_length_str.__doc__)
        characters_based_length_str()
    elif task_number == 35:
        print(forms_string_of_10_characters.__doc__)
        forms_string_of_10_characters()
    elif task_number == 43:
        print(search_numbers_in_string.__doc__)
        search_numbers_in_string()
    elif task_number == 51:
        print(string_matching.__doc__)
        string_matching()
    elif task_number == 59:
        print(change_word.__doc__)
        change_word()
    elif task_number == 0:
        exit()
    else:
        print('Неправильный ввод повторите')
    choice_number()


choice_number()


