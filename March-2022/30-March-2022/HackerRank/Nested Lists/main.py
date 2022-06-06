if __name__ == '__main__':
    lis_stu = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        lis_stu.append([name, score])
    second_high = sorted(list(set([score for name, score in lis_stu])))[1]
    print('\n'.join([name for name, score in sorted(
        lis_stu) if score == second_high]))
