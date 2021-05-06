def kgv(k, v):
    global counter
    if k == v:
        return k
    elif k > v:
        return kgv(k-v, v)
        counter=counter+1
    else:
        return kgv(k, v-k)
        counter=counter+1
    print(counter)
    return k*counter


zahl1=1
zahl2=2
counter=0
print("Das KGV von ", zahl1, " und ", zahl2, " ist ", kgv(zahl1, zahl2))
