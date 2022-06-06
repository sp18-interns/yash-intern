if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l = []
    # print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

    print([[i, j, k] for i in range(x+1) for j in range(y+1)
          for k in range(z+1) if((i+j+k) != n)])
