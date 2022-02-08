from typing import List

"""
Insertion_sort:
簡単で有名
・隣同士を比較していき、入れ替えがあれば小さい方をtempに保持する
・逆行しながらtempが適切な位置にくるまでバックしていく
・そこからまた進んでいく

>>> for i in range(1, 6):
...     j = i -1
...     while j >= 0:
...         print(j, end=' ')
...         j -= 1
...     print()
... 
0 
1 0 
2 1 0 
3 2 1 0 
4 3 2 1 0 


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


if __name__ == '__main__':
    import random

    nums = [random.randint(0,1000) for _ in range(10)]
    print(insertion_sort(nums))