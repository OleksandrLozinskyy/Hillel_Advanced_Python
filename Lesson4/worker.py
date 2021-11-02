f_name = 'input.txt'
o_name = 'output.txt'

gen_range = [i for i in range(1, 101)]


def get_denominator(file_name) -> int:
    """
    Функция принимает имя файла, пытается открыть его для чтения. В случае
    успеха считывается содержимое и конвертируется в целое число. Если в файле
    содержится не число, ноль или отрицательное число то выводится сообщение.
    Также выводится сообщение в случае, если не удалось открыть файл.
    :param file_name: файл для чтения параметра
    :return: Возвращает считанное число, если оно входит в заданный диапазон.
    Если число находится вне диапазона возвращает -1
    """
    try:
        with open(file_name, 'r', encoding='utf-8') as in_file:
            result = int(in_file.read())
            if result == 0:
                raise ZeroDivisionError
            elif result in gen_range:
                return result
            else:
                print(f"Incorrect number in file {file_name}")
                return -1
    except ZeroDivisionError:
        print(f"0 is not suitable number in file {file_name}")
    except IOError:
        print(f"File {file_name} not accessible")
    except ValueError:
        print(f"File {file_name} not contain number")


def get_list_of_numbers(denominator) -> list:
    """
    Функция проверяет делится ли число из списка на число передаваемое как
    параметр. Если остаток от деления 0, то число записывается в результирующий
    список. Возвращает список чисел, которые делятся без остатка.
    :param denominator: Делитель
    :return: Список чисел, которые делятся на делитель без остатка
    """

    res_range = [num for num in gen_range if num % denominator == 0]
    return res_range


def get_sum(list_of_numbers) -> int:
    """
    Функция принимает как аргумент список чисел, возвращает сумму всех чисел
    списка
    :param list_of_numbers: Список чисел
    :return: Сумма чисел списка
    """
    #    Вариант решения согласно начального курса
    #    accumulator = 0
    #    for x in list_of_numbers:
    #        accumulator += x
    #    return accumulator
    return sum(list_of_numbers)


def write_result(number, name_of_result_file='out.txt'):
    """
    Записывает число переданное в виде первого параметра в файл с названием,
    которое указано во втором параметре
    :param number: Число для записи
    :param name_of_result_file: Название файла для записи
    """
    try:
        with open(name_of_result_file, 'w', encoding='utf-8') as out_file:
            out_file.write(str(number))
            print(f"Success operation. File {name_of_result_file} writen")
    except IOError:
        f"File {name_of_result_file} writing not success, please check " \
            f"parameters"


divider = get_denominator(f_name)

if type(divider) == int and divider != -1:
    res_list = get_list_of_numbers(divider)
    total = get_sum(res_list)
    print(res_list)
    print(total)
    write_result(total, o_name)
else:
    print("Failure operation, please check parameters and try again. "
          "Additional information about error you can see above")
