for _ in range(3):
    n = list(map(int , input().split()))
    
    be = n.count(0)
    deung = n.count(1)
    
    if be == 1 and deung == 3:
        print("A")
    elif be == 2 and deung == 2:
        print("B")
    elif be == 3 and deung == 1:
        print("C")
    elif be == 4 and deung == 0:
        print("D")
    else:
        print("E")