from typing import List

"""
Select Sort:
シンプルでメジャーなソートなので押さえておくといい
・探索の始点の数値(のインデックス)をtmpに保持し、大小を比較していく
・保持した値より小さい値があれば(インデックスを)tmpを置き換える
・最終的にtmpに残ったインデックスの値と始点の値を入れ替える
・始点をひとつずらし繰り返していく
"""


def selection_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    for i in range(len_numbers):
        min_idx = i  # 一旦保持する値のidx(始点)
        for j in range(i+1, len_numbers):
            if numbers[min_idx] > numbers[j]:
                # 保持した値より小さい値があれば(idxを)更新していく
                min_idx = j
        # 終点まできたら最小値と始点の値を入れ替える
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(selection_sort(nums))