# Enter your code here. Read input from STDIN. Print output to STDOUT
n, li = int(input()), input().split()
print(all([int(i) > 0 for i in li]) and any([j == j[::-1] for j in li]))
