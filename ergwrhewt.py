import random

def feltoltes(a,n):
    for i in range(0,n):
        a.append(random.randint(0,100))

def kiiras(a,n):
    for i in range(0,n):
        print(a[i], end=", ")

def osszegzes(all,n):
    s = 0
    for i in range(0,n):
        s += a[i]
    return(s)

def min_ker(a,n):
    s = 0
    for i in range(0,n):
        if(a[i] < a[s]):
            s = 1
    return(s)

def max_ker(a,n):
    s = 0
    for i in range(0,n):
        if(a[i] > a[s]):
            s = 1
    return(s)

def tul_fuggv(x):
    return(((x%2)>0) and (x > 80) and (x < 90))

def lin_ker(a,n,T):
    i = 0
    while((i<n) and (not T(a[i]))):
     i+=1
    if(i<n):
        return(i)
    else:
        return(-1)


a = []
n = 100

feltoltes(a,n)
kiiras(a,n)
print()
print("Az elemek összege : {0}.".format(osszegzes(a,n)))
x = min_ker(a,n)
print("A legkisebb elem sorszáma : {0}.".format(x))
print("A legkisebb elem értéke : {0}.".format(a[x]))

x = max_ker(a,n)
print("A legnagyobb elem sorszáma : {0}.".format(x))
print("A legnagypbb elem értéke : {0}.".format(a[x]))

x = lin_ker(0,n,tul_fuggv)
if(x == -1):
    print("Nem találtuk meg az elemet!")
else:
    print("A megtalált elem sorszáma : {0}.".format[x])
