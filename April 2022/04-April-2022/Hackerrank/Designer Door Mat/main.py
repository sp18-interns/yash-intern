# Enter your code here. Read input from STDIN. Print output to STDOUT
N, M = map(int, input().split(' '))
for x in range(N):
    pattern = '.|.'
    if x < (N-1)/2:
        print((pattern*(2*x+1)).center(M, '-'))
    elif x == (N-1)/2:
        print('WELCOME'.center(M, '-'))
    else:
        print((pattern*(2*(N-1-x)+1)).center(M, '-'))

        #     print('-'*((M//2)-(2*(x+1))) + '.|.'*(2*(x+1))+'-'*((M//2)-(2*(x+1))),end='')
#     print()
# print('-'*((M-7)//2)+'WELCOME'+'-'*((M-7)//2))

# for x in range(0,N//2):

#     print('-'*((M//2)-(2*(x+1))) + '.|.'*((2*x)+1)+'-'*((M//2)-(2*(x+1))),end='')
#     print()
