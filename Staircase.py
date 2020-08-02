def staircase(n):
    for i in range(1, n+1):
        st = " "*(n-i)
        st += "#"*(i)
        print(st)
if __name__ == '__main__':
    n = int(input())

    staircase(n)
