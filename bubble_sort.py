from typing import List

"""
Bubble_sort:
・Listの先頭から[i]と[i+1](右隣)を比べる
・[i]の方が大きい場合は数値を入れ替える
・ひとつずつ移動しながら端まで繰り返す -> リスト内の最大値が最後にくる
・探索の上限をひとつ手前にずらす
・最後のひと組を比較するまで繰り返す
"""


def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):  # iを探索の上限値と解釈する
            if numbers[j] > numbers[j+1]:
                # [j]の方が大きければ左右を入れ替える
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    # nums = [2, 5, 1, 8, 7, 3]
    print(bubble_sort(nums))