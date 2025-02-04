import sys
N = int(sys.stdin.readline())

stack = []

for _ in range (N):
    stack.append(int(sys.stdin.readline()))

last = stack[-1]
count = 1

for i in reversed(range(N)):
    if stack[i] > last:
        count += 1
        last = stack[i]

print(count)