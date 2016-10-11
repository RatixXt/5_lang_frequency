# -*- coding: utf-8 -*-
from os.path import exists
from re import findall
from collections import Counter
from codecs import open


def load_data(filepath):
    if exists(filepath):
        with open(filepath, 'r', 'utf-8') as file_handler:
            return file_handler.read()


def get_most_frequent_words(text):
    words = findall(r'[a-я]\w+|[a-z]\w+', text.lower())
    return Counter(words).most_common(10)


def get_filepath():
    return input(u"Введите путь к файлу:")


if __name__ == '__main__':
    filepath = get_filepath()
    data = load_data(filepath)
    if data is not None:
        common_words = get_most_frequent_words(data)
        print(common_words)
    else:
        print(u'Данных нет или указан неверный путь к файлу')
