def swap_case(s):
    swap_s = ''
    for letter in s:
        if letter.islower():

            swap_s += letter.upper()
        elif letter.isupper():

            swap_s += letter.lower()
        else:
            swap_s += letter
    return swap_s


if __name__ == '__main__':
