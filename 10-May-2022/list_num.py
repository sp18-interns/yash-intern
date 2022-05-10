def check_sum_target(lis = list(),target=0):
    length= len(lis)
    for i in range(len(lis)):
        for j in range(1,len(lis)):
            if lis[i]+lis[j]== target:
                return lis[i],lis[j]
    else:
        return(f'Sum of any elements of this list is not equal to target')