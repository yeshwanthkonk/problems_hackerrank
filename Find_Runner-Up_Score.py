if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ma1 = -101
    ma2 = -101
    for i in arr:
        if(ma1==i):
            continue
        elif(ma1<i):
            ma2 = ma1
            ma1 = i
        elif(ma2<i):
            ma2 = i
    print(ma2)
