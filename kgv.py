def ggt(k, v):
    if k == v:
        return k
    elif k > v:
        return ggt(k-v, v)
    else:
        return ggt(k, v-k)

def kz(x, y):
    if x > y:
        return y
    else:
        return x

def kgv(m, n, o):
    if n > o:
        return n*(o/m)
    else:
        return o*(n/m)


zahl1=1
zahl2=2
counter=0
ggt = ggt(zahl1, zahl2)
print("Das KGV von ", zahl1, " und ", zahl2, " ist ", kgv(ggt, zahl1, zahl2))
