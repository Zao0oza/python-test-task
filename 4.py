import json
import argparse


def count_questions(data: dict):
    print(len(data['game']['rounds'][1]['questions'][1]))


# вывести количество вопросов (questions)


def print_right_answers(data: dict):
    for i in data['game']['rounds'][1]['questions']:
        print(i["correct_answer"])
    # вывести все правильные ответы (correct_answer)


def print_max_answer_time(data: dict):
    time_to_answer = []
    for i in data['game']['rounds'][1]['questions']:
        time_to_answer.append(i['time_to_answer'])
    print(max(time_to_answer))
    # вывести максимальное время ответа (time_to_answer)


def main(args):
    with open(args, "r") as read_file:
        data = json.load(read_file)
    # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    # передать имя файла из аргументов командной строки

    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=str, help='name of file')
    args=parser.parse_args()
    main(args.file)