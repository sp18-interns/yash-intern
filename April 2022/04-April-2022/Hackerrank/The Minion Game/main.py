def minion_game(string):
    # your code goes here
    Stuart, Kevin = 0, 0

    for letter in range(len(string)):
        if string[letter] in 'aeiouAEIOU':
            Kevin += (len(string)-letter)
        else:
            Stuart += (len(string)-letter)
    if Stuart > Kevin:
        print(f'Stuart {Stuart}')
    elif Kevin > Stuart:
        print(f'Kevin {Kevin}')
    else:
        print('Draw')


if __name__ == '__main__':
