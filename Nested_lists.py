from functools import cmp_to_key
if __name__ == '__main__':
    arr = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        arr.append([name, score])
    # fi = 101
    # se = 101
    # for i in range(len(arr)):
    #     if(arr[i][1]<fi):
    #         se = fi
    #         fi = arr[i][1]
    #     elif(arr[i][1] > fi and arr[i][1] < se):
    #         se = arr[i][1]

    # arr2 = []
    # for i in range(len(arr)):
    #     if(arr[i][1] == se):
    #         arr2.append(arr[i][0])
    # arr2.sort()
    # for i in arr2:
    #     print(i)
    
    def func(a, b):
        if(a[1] == b[1]):
            if(a[0]>b[0]):
                return 1
            else:
                return -1
        else:
            return a[1] - b[1]



    arr = sorted(arr, key=cmp_to_key(func))
    i = 0
    while(arr[i][1] == arr[i+1][1]):
        i += 1
    i += 1
    while(i<len(arr)-1 and arr[i][1] == arr[i+1][1]):
        print(arr[i][0])
        i += 1
    print(arr[i][0])
        
