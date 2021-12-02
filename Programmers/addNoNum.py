# Counter 컬렉션은 서로 뺄 수 있다
# Counter로 뺀 뒤 sum 해서 계산

from collections import Counter


def solution(numbers):
    answer = -1
    numSet = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    answer = sum(Counter(numSet) - Counter(numbers))
    return answer
