COL = int(input())
qw = []
we = []
for  k in range(COL):
    Q, W = input().split(' ')
    W = str(W)
    Q = int(Q)
    qw.append(Q)
    we.append(W)

for j in range(len(qw)):
    D = qw[j]
    P = we[j]

    PM = []
    for i in P:
        PM.append(i)

    o = ''.join(sorted(PM))
    o = o[::-1]
    #All damage
    def main(PM):
        power = 1
        damage = 0
        for i in range(len(PM)):
            if PM[i] == 'C':
                power *=2
            if PM[i] == 'S':
                damage += power
        return damage

    #Other
    now = main(P)
    n = 0
    while now > D:
        t = ''.join(PM)
        if t == o:
            break
        t=''
        for i in range(len(PM)):
            if i != len(PM)-1:
                if PM[i] + PM[i+1] == 'CS':
                    PM[i], PM[i+1] = PM[i+1], PM[i]
                    n+=1
                    now = main(PM)
                    i=0


    if now > D:
        print('Case #{}: IMPOSSIBLE'.format(j+1))
    else:
        print('Case #{}: {}'.format(j+1,n))
