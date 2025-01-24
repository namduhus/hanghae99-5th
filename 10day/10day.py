# 문제: 백준 32953번 문제 회상

import sys
input = sys.stdin.readline


# 첫번째 줄

N, M = map(int, input().split()) # 수업 수 N, 최소 등장 횟수M

# 두번째 줄
student_count = {} # 학번 등장 횟수 저장 딕셔너리

for _ in range(N):
    K = int(input().strip())
    student_nums = input().strip().split()
    
    for number in student_nums:
        if number in student_count:
            student_count[number] += 1
        else:
            student_count[number] = 1

result = sum(1 for count in student_count.values() if count >= M)

print(result)