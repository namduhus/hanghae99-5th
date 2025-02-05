import sys
N = int(sys.stdin.readline())

stack = []

for _ in range(N):
    come = sys.stdin.readline().strip().split()

    if come[0] == 'push':
        stack.append(come[1])
    
    elif come[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    
    elif come[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif come[0] == 'size':
        print(len(stack))
    
    elif come[0] == 'front':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    
    elif come[0] == 'back':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])

print("끝")