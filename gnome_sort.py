from typing import List

"""
Gnome sort:
bubble sortに類似
・隣り合った数値を比べていき、右が小さければ入れ替える
・コード的にはbubble sortと違い、ひとつ手前の数値と比較している
・入れ替えが起きた場合、ひとつ手前に戻り再度比較する
・最小値がどんどん始点に追いやられていく
・戻りなく終点にくればソート完了
"""


def gnome_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    index = 0
    while index < len_numbers:
        if index == 0:
            # while一週目は手前に比較対象がいないのでindex + 1して二週目にいく
            index += 1
        if numbers[index] >= numbers[index-1]:
            # indexの手前の方が小さければ次のターンへ
            index += 1
        else:
            numbers[index], numbers[index-1] = numbers[index-1], numbers[index]
            # 入れ替えが発生したらindex - 1して手前に戻る
            index -= 1

    return numbers


if __name__ == '__main__':
    import random

    nums = [random.randint(0, 1000) for _ in range(10)]
    print(gnome_sort(nums))