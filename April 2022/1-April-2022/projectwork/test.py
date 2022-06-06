N, X = map(int, input().split())
marks = []
for _ in range(X):
    marks.append(map(float, input().split()))

[print(sum(i)/len(i)) for i in zip(*marks)]
