import os
import re
import threading


def task1():
    path = os.getcwd()
    name = "filenames.txt"
    i = 0
    for root, dirs, files in os.walk(path + '/test'):
        if name in files:
            i += 1
    print("filenames -", i)
    # в папке test найти все файлы filenames вывести колличество


def task2():
    # в папке test найти все email адреса записанные в файлы
    '''
    возвращает список всех файлов
    '''
    files_list = []

    path = os.getcwd()
    for root, dirs, files in os.walk(path + '/test'):
        for name in files:
            if name:
                files_list.append(os.path.join(root, name))
    return files_list


def find(filename):
    """
    Принимает имя файла, ищет в нем email,
    возвращет email
    """
    regex = re.compile(
        r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    with open(filename, 'r') as file:
        for string in file:
            if re.search(regex, string):
                print(string)


def main():
    task1()

    for filename in task2():
        my_thread = threading.Thread(target=find(filename))
        my_thread.start()
    # дополнительно: придумать над механизм оптимизации 2-й задачи (используя threading)


if __name__ == '__main__':
    main()
