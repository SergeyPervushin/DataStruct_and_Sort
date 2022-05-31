
import string
from random import randint, choice
from work import time_decorator
import typing as t


def iterate_by(num: t.Iterable[int]) -> None:
    for n in num:
        print(n)


iterate_by([1, 2, 3, 4])
iterate_by(range(1_00))
iterate_by('duck')


class List_for_test:
    def __init__(self, size) -> object:
        self.size = size

    def nums_random(self):
        l = []
        for i in range(0, self.size):
            l.append(randint(0, self.size))
        return l

    def rendom_chrs(self):
        letters = string.ascii_lowercase
        random_chrs = [choice(letters) for i in range(self.size)]
        return random_chrs

    def ascending_sorted(self):
        l = [i for i in range(0, self.size)]
        return l

    def descending_sorted(self):
        l = [i for i in range(self.size, 0, -1)]
        return l


def bubble_sort(data_set):
    pass


@time_decorator
def binary_search(data, desired_item):
    if len(data) == 1:
        return data[0]

    begin = 0
    end = len(data) - 1
    mid = 0
    while begin < end:
        mid = (end + begin) // 2 - 1
        if data[mid] == desired_item:
            break
        if desired_item < data[mid]:
            end = mid - 1

        else:
            begin = mid + 1

    return f'desire item index = {mid}'


@time_decorator
def linear_search(data, desired_item):

    for i in range(len(data)):
        if data[i] == desired_item:
            return f'desired item index is {i}'
    return f'there is no {desired_item}'


