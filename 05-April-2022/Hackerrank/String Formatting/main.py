
def print_formatted(number):
    # your code goes here
    result = []
    for i in range(1, number+1):
        #     # print(f'{i} {str(oct(i))} {str(hex(i))} {str(bin(i))}' )
        #     #print(i,oct(i),hex(i),bin(i) )

        decimal = str(i)
        octal = (oct(i))[2:]
        hexadecimal = ((hex(i))[2:]).upper()
        binary = (bin(i))[2:]

        result.append([decimal, octal, hexadecimal, binary])
    width = len(result[-1][3])

    for x in result:
        print(*(y.rjust(width) for y in x))
