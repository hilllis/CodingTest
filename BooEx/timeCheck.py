########################################
# 시간 체크 문제                       #
# 제한시간 15분 시간 제한 2초 메모리 제한 128MB#
#######################################
# 문제 요약
# 정수 N이 입력되면 00시 00분 00초부터  N시 59분 59초까지의 모든 시각중에서 3이 하나라도 포함되는 모든 경우의 수 구하기

#########################################
# 내 아이디어
# 59초까지의 모든 3포함 숫자 세기, 59분까지의 모든 3포함 숫자 세기, N까지의 모든 3포함 숫자 세기

n = int(input())
count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            # 문자열로 변환해서 3이 있는지 체크
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
