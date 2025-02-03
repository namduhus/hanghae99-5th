import sys

N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    come = sys.stdin.readline().split()

    if come[0] == 'push':
          stack.append(come[1])
    elif come[0] == 'pop':
          if len(stack) == 0:
               print(-1)
          else:
               print(stack.pop())
    elif come[0] == 'size':
         print(len(stack))
    elif come[0] == 'empty':
         if len(stack) == 0:
              print(1)
         else:
              print(0)
    elif come[0] == 'top':
         if len(stack) == 0:
              print(-1)
         else:
              print(stack[-1])