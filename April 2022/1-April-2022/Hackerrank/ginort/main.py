# Enter your code here. Read input from STDIN. Print output to STDOUT
s = input()
upper, lower, number, special = 0, 0, 0, 0
upper_case, lower_case, odd_digit, even_digit = [], [], [], []
for i in range(len(s)):
    if s[i].isupper():
        upper += 1
        upper_case.append(s[i])
    elif s[i].islower():
        lower += 1
        lower_case.append(s[i])
    elif s[i].isdigit():
        number += 1
        if int(s[i]) % 2 == 0:
            even_digit.append((s[i]))
        else:
            odd_digit.append((s[i]))

    lower_case.sort()
    upper_case.sort()
    even_digit.sort()
    odd_digit.sort()
print("".join(lower_case)+"".join(upper_case) +
      "".join(odd_digit)+"".join(even_digit))
