# 내 아이디어:
# n을 3으로 나누면 몫과 나머지가 나오는데 몫을 124나라의 수로 바꾼 값과 각 나머지를 문자열로 더한 값과 같다.
# 또한 나머지가 없는 경우에는 n-1 한 값을 전환한 수에 2를 더한 값이 나온다.

def solution(n):
    answer = str(logic(n))

    return answer


def logic(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4

    if num % 3 == 0:
        num = logic(num-1) + 2
    elif num % 3 == 1:
        num = logic(int(num/3)) * 10 + 1
    elif num % 3 == 2:
        num = logic(int(num/3)) * 10 + 2

    print(num)
    return num
