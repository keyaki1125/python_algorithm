from typing import List

"""
Bucket sort:
insertion sortを使用。
・任意の要素数のリスト（バケット）を用意
・今回はリスト内の最大値を10で割った、10個のリストにする
・バケット[0]には10で割って商が0のものを、バケット[1]には10で割って商が1のものを振り分けていく
・二次元配列のバケットの各要素内でinsertion sortをかける。
・バケット内の値を連結する
"""


def insertion_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(1, len_numbers):
        temp = numbers[i]  # 入れ替えがあればこの値が前に進んでいく
        j = i - 1
        while j >= 0 and numbers[j] > temp:
            numbers[j+1] = numbers[j]  # numbers[j+1]はtempと同じ(tempは更新したくない)
            j -= 1  # -1でnumbers[j] > tempになるまでバックしていく

        numbers[j+1] = temp

    return numbers


def bucket_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers  # bucketの要素数となる(//は割り算の整数部分を返す)
    buckets = [[] for _ in range(size)]  # リスト内包表記

    for num in numbers:
        i = num // size  # 要素を10で割る
        if i != size:  # 今回の場合、10台は1に、20台は2というふうに振り分けられる、
            buckets[i].append(num)
        else:  # size以上のもの（今回は100）は一つ手前に振り分ける
            buckets[size - 1].append(num)

    for i in range(size):
        # bucket各要素内でinsertion sortをかける
        insertion_sort(buckets[i])

    result = []
    for i in range(size):
        # resultにバケット内の値を連結していく
        result += buckets[i]

    return result


if __name__ == '__main__':
    import random

    nums = [random.randint(0, 1000) for _ in range(10)]
    # nums = [1, 5, 28, 25, 100, 52, 27, 91, 22, 99]
    print(bucket_sort(nums))