def countup(k):
    if k == 0:
        print(k)
    else:
        print(k)
        countup(k+1)

countup(5)


def countup2(k):
    if k :
        return 0
    else:
        return k+countup2(k-1)

y=5
countup2(y)


zahl=5
countup3(zahl)

def countup3(k):
    if k=zahl:
        check = 1
        countup3(0)
    if k<zahl:
        print(k)
        countup3(k+1)
