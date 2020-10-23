""" https://www.codewars.com/kata/5f6d533e1475f30001e47514 """


def consecutive(arr, a, b):
    for item in range(0, len(arr) - 1):
        if arr[item] == a:
            is_b_next = arr.index(arr[item + 1])

            if arr[is_b_next] == b:
                return True

        elif arr[item] == b:
            is_a_next = arr.index(arr[item + 1])

            if arr[is_a_next] == a:
                return True

    return False
