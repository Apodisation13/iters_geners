import json
import wikipedia
from os import path
import hashlib


class IterCountries:
    def __init__(self, number):
        self.number = number - 1  # -1 для удобства отображения числа
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter <= self.number:
            wiki_search(file, counter=self.counter)
            self.counter += 1
            return
        else:
            raise StopIteration


def wiki_search(file, counter):
    with open('output_file.txt', 'a+', encoding='utf-8') as out:
        off_name = file[counter]['name']['official']
        link = wikipedia.WikipediaPage(off_name).url
        out.write(f'Страна - {off_name}, ссылка на вики - {link}\n')
        print(f'Страна {off_name} внесена в файл')


def input_json_reader(json_file: str):
    with open(json_file) as input_json:
        input_list = json.load(input_json)
    return input_list


def hash_gen(f):
    # line = (f.readline())
    yield hashlib.md5(f.encode()).hexdigest()


file = input_json_reader('countries.json')  # общий файл в куче в виде списка
c = [country for country in IterCountries(12)]

file_path = path.abspath('output_file.txt')

with open(file_path, encoding='utf-8') as f:
    for line in f:
        print(*hash_gen(line))

    # print(*hash_gen(f))  # Второй способ, надо открыть строку 39
    # print(*hash_gen(f))
