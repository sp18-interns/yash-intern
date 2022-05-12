n, m = map(int, input().split())
sum = 0
N = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = A | B
N = (i for i in N if i in C)
for i in N:
    if i in A:
        sum += 1
    else:
        sum -= 1
print(sum)
