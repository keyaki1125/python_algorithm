import random
from typing import List


def in_order(numbers: List[int]) -> bool:  # python3は引数と返り値の期待される型を表記できる
    # リストのi番目とi+1番目(右隣)を比べて全て右側の方が大きければTrueを返す
    return all(numbers[i] <= numbers[i + 1] for i in range(len(numbers) - 1))
    # このforループは上のように書き換えられる
    # for i in range(len(numbers)-1):
    #     if numbers[i] > numbers[i+1]:
    #         return False
    # return True


def bogo_sort(numbers: List[int]) -> List[int]:  # typing.Listを利用するとリストの中身も指定できる(python3.5以上)
    # in_order()でTrueが出るまで(全て右側が大きくなるまで)シャッフルし続ける
    while not in_order(numbers):
        random.shuffle(numbers)
    return numbers


if __name__ == '__main__':
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(bogo_sort(nums))
    # print(bogo_sort([1, 5, 3, 2, 6]))