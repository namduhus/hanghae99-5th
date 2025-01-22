# 문제: 백준 32978번 문제 아 맞다 마늘

import sys
input = sys.stdin.readline

# 첫 번째 줄: 재료의 총 개수 N
N = int(input())

# 두 번째 줄: 봉골레 파스타에 들어가는 N개의 재료
pasta = set(input().strip().split())

# 세 번째 줄: 현빈이가 사용한 N-1개의 재료
hyunbin = set(input().strip().split())

# 누락된 재료 찾기 (차집합)
missing = pasta - hyunbin

# 출력
print(missing.pop())