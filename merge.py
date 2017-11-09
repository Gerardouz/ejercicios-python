def Mezclar (a,b):

    la,lb = len(a),len(b)
    i,j = 0,0
    c = []
    while (i < la and j < lb):
        
        if (a[i] < b[j]):
            c.append(a[i])
            i = i + 1
        else:
            c.append(b[j])
            j = j + 1
    
    while (i < la):
        c.append(a[i])
        i = i + 1
    
    while (j < lb):
        c.append(b[j])
        j = j + 1
    
    return c


def OrdMerge (a):
    pf = len(a)-1
    
    if (pf == 0):
        return a
    
    pm = pf/2
    a1 = OrdMerge (a[:pm+1])
    a2 = OrdMerge (a[pm+1:pf+1])
    return  Mezclar (a1,a2)

# PRINCIPAL

a = [4,2,5,8,1,3,9,7,6,12,0] 

print a
a = OrdMerge(a)
print a