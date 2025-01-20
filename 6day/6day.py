# 문제: 백준 27160 할리갈리

# 입력
# 첫 번째 줄에 펼쳐진 카드의 개수 $N$이 주어집니다.
# 두 번째 줄부터 $N$개의 줄에 걸쳐 한 줄에 하나씩 펼쳐진 카드의 정보가 주어집니다.
# 카드의 정보는 공백으로 구분된, 과일의 종류를 나타내는 문자열 $S$와 과일의 개수를 나타내는 양의 정수 $X$로 이루어져 있습니다.
# $S$는 STRAWBERRY, BANANA, LIME, PLUM 중 하나입니다.

# 출력
# 한별이가 종을 쳐야 하면 YES을, 아니면 NO를 출력해주세요.


import sys
input = sys.stdin.readline

N = int(input().strip())
fruit_count = {
    'STRAWBERRY': 0,
    'BANANA': 0,
    'LIME': 0,
    'PLUM': 0
}

for _ in range(N):
    S, X = input().split()
    X = int(X)
    fruit_count[S] += X

if 5 in fruit_count.values():
    print("YES")
else:
    print("NO")