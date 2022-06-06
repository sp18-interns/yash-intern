number_of_stamps = input()
distinct = set()
for i in range(int(number_of_stamps)):
    distinct.add(input())
print(len(distinct))