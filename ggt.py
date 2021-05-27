def ggt(k, v):
    if k == v:
        return k
    elif k > v:
        return ggt(k-v, v)
    else:
        return ggt(k, v-k)


zahl1 = 1
zahl2 = 3
print(ggt(zahl1,zahl2))
