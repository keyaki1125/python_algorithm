from typing import List

"""
Comb_sort:
Combはクシという意味。
・gapという変数を用意する
・gap = リストの要素数 / 1.3(決まっている値) (小数点以下切り捨て)
・[i]と[i+gap]同士を比較、[i]が大きければ入れ替える
・最後尾まで来たらgapをさらに1.3で割り、[i]と[i+gap]の比較を繰り返す
・gapは小さくなっていき、gap=1になったら変数swappedを用意する
・[i]と[i+gap](gap=1なので隣同士)を比較し、swapped=Falseのまま終端まできたら並べ替え完了
"""


def comb_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
                swapped = True

    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(comb_sort(nums))