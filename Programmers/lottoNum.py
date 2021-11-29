########################################
# 로또 순위 문제                          #
#######################################
# 문제 요약
# 로또 번호 6개와 당첨 번호 6개 씩 입력 받는데, 입력 받는 로또 번호는 부분 부분 지워진 곳 존재
# 지워진 부분은 0으로 표시 됨
# 지워진 부분 포함해서 당첨될 수 있는 가장 좋은 순위
# 지워진 부분 포함해서 당첨될 수 있는 가장 나쁜 순위 두 가지 출력
# #########################################
# 내 아이디어
# lotto에서 당첨 번호와 같은 개수가 최저
# lotto에서 0의 개수를 더하면 최대


def solution(lottos, winNums):
    winCnt = 0
    zeroCnt = 0

    for i in range(len(lottos)):
        if lottos[i] == 0:
            zeroCnt += 1
            continue
        for j in range(len(winNums)):
            if lottos[i] == winNums[j]:
                winCnt += 1

    answer = []

    answer.append(order(winCnt + zeroCnt))
    answer.append(order(winCnt))
    return answer


def order(orderNum):
    answer = 0

    if orderNum == 6:
        answer = 1
    elif orderNum == 5:
        answer = 2
    elif orderNum == 4:
        answer = 3
    elif orderNum == 3:
        answer = 4
    elif orderNum == 2:
        answer = 5
    else:
        answer = 6
    return answer


lottos = list(map(int, input().split()))
win_nums = list(map(int, input().split()))

print(solution(lottos, win_nums))
