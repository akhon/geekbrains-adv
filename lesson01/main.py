#!/usr/bin/env python3
import subprocess
import pickle

list1 = ['разработка', 'сокет', 'декоратор']

list1_utf16 = [
    '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
    '\u0441\u043e\u043a\u0435\u0442',
    '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
]

list2 = ['class', 'function', 'method']

list3 = ['attribute', 'класс', 'функция', 'type']

list4 = ['разработка', 'администрирование', 'protocol', 'standard']

list5 = ['yandex.ru', 'youtube.com']

list6 = ['сетевое программирование', 'сокет', 'декоратор']


def print_vars_types(str_list):
    for item in str_list:
        print("значение: ", item, ", тип: ", type(item))


# done
def subtask01():
    print("=== subtask01 ===")
    print("human-readable list of strings:")
    print_vars_types(list1)

    print("utf16 list of strings:")
    print_vars_types(list1_utf16)


#done
def subtask02():
    print("=== subtask02 ===")
    bytes_list = []
    for item in list2:
        bytes_list.append(pickle.dumps(item))

    for item in bytes_list:
        print("значение: ", item, " тип: ", type(item), " и длина: ", len(item))


# done
def subtask03():
    print("=== subtask03 ===")
    for string in list3:
        try:
            print(type(string.encode())
        except UnicodeEncodeError:
            print("строка {} не может быть преобразована в байтовое представление".format(string))


# done
def subtask04():
    print("=== subtask05 ===")
    for string in list4:
        string_encoded = string.encode()
        print(string_encoded.decode())


# done
def subtask05():
    print("=== subtask04 ===")
    for host in list5:
        # i'm unix user, ping command is infinite
        args = ['ping', '-c 1']
        args.append(host)
        subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in subproc_ping.stdout:
            line = line.decode('cp866').encode('utf-8')
            print(line.decode('utf-8'))


# done
def subtask06():
    print("=== subtask06 ===")
    f_n = open("test_file.txt", "w")
    f_n.write('сетевое программирование сокет декоратор')
    f_n.close()
    print(f_n)

    with open('test_file.txt', encoding='utf-8') as f_n:
        for el_str in f_n:
            print(el_str, end='')
    f_n.close()


def main():
    subtask01()
    subtask02()
    subtask03()
    subtask04()
    subtask05()
    subtask06()


if __name__ == '__main__':
    main()
