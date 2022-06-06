if __name__ == '__main__':
    N = int(input())
    li = []
    for _ in range(N):
        x = input().split()
        cmd = x[0]
        args = x[1:]
        if cmd != 'print':
            cmd += "(" + ",".join(args) + ")"
            eval("li."+cmd)
        else:
            print(li)
