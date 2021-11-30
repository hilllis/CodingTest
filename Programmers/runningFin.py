# 프로그래머스 완주하지 못한 선수 문제
# 딕셔너리 만들어서 participant에 있는 참가자 이름을 키 값으로 카운트를 밸류로 넣기
# completion에서 이름 있으면 밸류 -1 하기
# 남아있는 친구 answer에 넣어주고 반환

def solution(participant, completion):
    answer = ''
    dictRun = {}

    for i in range(len(participant)):
        if participant[i] in dictRun:
            dictRun[participant[i]] += 1
            continue
        d = {participant[i]: 1}
        dictRun.update(d)

    for j in range(len(completion)):
        if completion[j] in dictRun:
            dictRun[completion[j]] -= 1

    for keys in dictRun:
        if dictRun[keys] > 0:
            answer += keys

    return answer
