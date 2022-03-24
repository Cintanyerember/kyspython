def neved(s):
    l = s.split()
    n = ""

    for i in range(len(l)-1):
        s = l[i]
        n += (s[0].upper()+'.')
        n += l[-1].title()
    return n
				
s = input("Név ")
print(neved(s))		
