import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
a = []
b = []

for _ in range(n):
    com = list(map(int, sys.stdin.readline().strip().split()))

    if com[0] == 1:
        queue.append((com[1], com[2]))

    else:
        x, y = queue.popleft()

        if y == com[1]:
            a.append(x)
        else:
            b.append(x)

a.sort()
b.sort()
c = sorted(list(queue))

if not a:
    print("None")
else:
    print(*a, sep=" ")

if not b:
    print("None")
else:
    print(*b, sep=" ")

if not c:
    print("None")
else:
    for i in c:
        print(i[0], end=" ")


