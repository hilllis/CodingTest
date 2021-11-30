# 프로그래머스 크레인 인형 뽑기 문제
# move 가 1 이면, board[i][0]의 맨 위칸 부터 0이 아닌 곳 까지 검색 후 나오면 stack에 삽입
# stack에 삽입하는데 stack의 맨 마지막 칸과 삽입하는 값이 같다면 pop
# moves가 끝나고 answer = len(stack)으로 계산

def solution(board, moves):
    answer = 0
    pickArr = []

    for i in range(len(moves)):
        dy = moves[i]
        for k in range(len(board)):
            if board[k][dy-1] != 0:
                if len(pickArr) > 0:
                    if pickArr[-1] == board[k][dy-1]:
                        pickArr.pop()
                        board[k][dy-1] = 0
                        answer += 2
                        break
                pickArr.append(board[k][dy-1])
                board[k][dy-1] = 0
                break

    return answer
