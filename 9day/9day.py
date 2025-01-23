# 문제: 백준 31562번 문제 전주 듣고 노래 맞히기

import sys
input = sys.stdin.readline

# 첫번째 줄
N, M = map(int, input().split())
song = {}

# 두번째 줄
for i in range(N):
    T, S, a1, a2, a3, a4, a5, a6, a7 = input().split()
    A = [a1, a2, a3]
    song[S] = A
    
for _ in range(M):
    B = input().split()
    count = 0
    title = ""
    
    for s in song:
        if B == song[s]:
          count += 1
          title = s
    
    if count >= 2:
        print("?")
    elif count == 1:
        print(title)
    else:
        print("!")
    