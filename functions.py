FILEPATH = 'todos.txt'
import random


def get_todos(filepath=FILEPATH):
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_list, filepath=FILEPATH):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_list)


def get_quote():
    quote_list = ["הכל שטויות", "אני מתה על הגן הזה", " אני צריכה עוד מקום אחסון", "זו לא תחנת מעבר", "הזמנתי לבלו נעליים", "תתנצל", "הכנתי קינוח"]
    quote = random.choice(quote_list)
    return quote
