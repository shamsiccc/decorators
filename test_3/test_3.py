import os.path
import types
from datetime import datetime


def logger(func):
    def wrapper(*args, **kwargs):

        func_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # запоминаем время начала
        result = func(*args, **kwargs)  # вызываем оригинальную функцию

        if os.path.exists('main.log'):
            os.remove('main.log')

        with open('main.log', 'a', encoding='utf-8') as f:
            f.write(f"Функция '{func.__name__}' выполнена с аргументами: {args}, {kwargs}. \n"
              f"Возвращаемое значение: {result}. \n"
              f"Время выполнения: {func_time} \n")

        return result

    return wrapper

@logger
def flat_generator_v5(list_of_list):
    for i in list_of_list:
        if isinstance(i, list):
            for j in flat_generator_v5(i):
                yield j
        else:
            yield i


def test_task_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator_v5(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator_v5(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator_v5(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':

    test_task_4()