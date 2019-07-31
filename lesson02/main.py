#!/usr/bin/env python3

import csv
import chardet
import json


# cut leading and trailing spaces, return string
def list_reformat(list):
    return "".join(str(e) for e in list).strip()


# convert list to string
def list_to_str(list):
    return str(list).strip('[\'\']')


def get_data():
    # input files
    # have to convert to utf8 first
    # chardet detects MacCyrillic which is not readable
    list_of_files = ['data/info_1_utf8.txt', 'data/info_2_utf8.txt', 'data/info_3_utf8.txt']

    main_data = []
    main_data.append(['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы'])
    for f_path in list_of_files:

        os_prod_list = []
        os_name_list = []
        os_code_list = []
        os_type_list = []

        # detecting encoding
        with open(f_path, 'rb') as f:
            f_info = chardet.detect(f.readline(16))
            f_encoding = f_info.get('encoding')

        f.close()

        # open file with detected encoding
        with open(f_path, 'r', encoding=f_encoding) as f:
            f_reader = csv.reader(f, delimiter="\t")
            for row in f_reader:
                for items in row:
                    if 'Изготовитель системы' in items.split(':')[:1]:
                        os_prod_list.append(list_reformat(items.split(':')[1:]))
                    if 'Название ОС' in items.split(':')[:1]:
                        os_name_list.append(list_reformat(items.split(':')[1:]))
                    if 'Код продукта' in items.split(':')[:1]:
                        os_code_list.append(list_reformat(items.split(':')[1:]))
                    if 'Тип системы' in items.split(':')[:1]:
                        os_type_list.append(list_reformat(items.split(':')[1:]))
        f.close()

        main_data.append([list_to_str(os_prod_list), list_to_str(os_name_list), list_to_str(os_code_list), list_to_str(os_type_list)])

    return(main_data)


def write_data(f):

    data = get_data()
    f_writer = csv.writer(f)
    for row in data:
        f_writer.writerow(row)


# done
def subtask01():
    with open('main_data_write.txt', 'w') as f_n:
        write_data(f_n)
    f_n.close()


def write_order_to_json(item, quantity, price, buyer, date):
    new_order = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date
    }

    # get data from file, append new order, write back into a file data with new order
    with open('data/orders.json', 'r+') as f:
        objs = json.load(f)

        for k,v in objs.items():
            if k == 'orders':
                v.append(new_order)

        f.seek(0)
        json.dump({k:v}, f, sort_keys=True, indent=4)

    f.close()


# done
def subtask02():
    write_order_to_json('thing', '2', '20', 'Vasya', '2019-07-31')
    write_order_to_json('other thing', '5', '10', 'Petya', '2019-07-30')


def subtask03():
    write_order_to_json('thing', '2', '20', 'Vasya', '2019-07-31')
    write_order_to_json('other thing', '5', '10', 'Petya', '2019-07-30')


def main():
    #subtask01()
    #subtask02()
    subtask03()


if __name__ == '__main__':
    main()