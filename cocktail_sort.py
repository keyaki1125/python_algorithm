from typing import List

"""
Cocktail_sort:
Bubble_sortの改良版
・バブルソート同様左右を比較しながら進む
・入れ替えが発生した場合、swap=Trueにする
・最後まで来たらendを一つ手前にずらして、startに向かって逆行する
・同じように入れ替えが発生したらswap=Trueにする
・startに戻ったらstartを一つ先に移動して同じことを繰り返す
・swap=Falseのまま端まで来たら入れ替え終了と判断する
"""


def cocktail_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    swapped = True # 最初はTrueにしとかないとwhileを回せない
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True  # 入れ替えたらTrueにする

        # 最後尾まで来てswapped = Falseのままであれば終了
        if not swapped:
            break
        # でなければswappedを初期化、endを一つ手前にずらす
        swapped = False
        end = end - 1

        for i in range(end-1, start-1, -1):  # endの一個前の一個前からstartの一個手前の次まで-1ずつ進む。
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True  # 入れ替えたらTrueにする

        start = start + 1

    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for i in range(10)]
    print(cocktail_sort(nums))