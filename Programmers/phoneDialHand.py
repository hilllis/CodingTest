# 0일 때는 L 2일 때는 R
# 1일 때는 가까운 거리에 있는 손
# 좌 우 거리는 항상 1이므로 높이로 거리 계산
# Left, Right 인덱스를 저장해 놓고 어디에 더 가깝나 비교,,,

def solution(numbers, hand):
    answer = ''
    # left right 인덱스 저장
    right = [3, 2]
    left = [3, 0]

    pad = ([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 0, 11]])

    for num in numbers:
        for i in range(len(pad)):
            if num == pad[i][0]:
                answer += 'L'
                left[0] = i
                left[1] = 0

            elif num == pad[i][2]:
                answer += 'R'
                right[0] = i
                right[1] = 2

            elif num == pad[i][1]:
                dLeft = abs(left[1] - 1) + abs(left[0] - i)
                dRight = abs(right[1] - 1) + abs(right[0] - i)

                if dLeft == dRight:
                    if hand == 'right':
                        answer += 'R'
                        right[1] = 1
                        right[0] = i

                    else:
                        answer += 'L'
                        left[1] = 1
                        left[0] = i

                elif dLeft < dRight:
                    answer += 'L'
                    left[1] = 1
                    left[0] = i

                elif dLeft > dRight:
                    answer += 'R'
                    right[1] = 1
                    right[0] = i

    return answer
