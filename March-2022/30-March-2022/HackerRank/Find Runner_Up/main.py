if '__name__' == '__main__':
    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]
    max_score = max(arr)
    while max(arr) == max_score:
        arr.remove(max(arr))
    print(max(arr))
