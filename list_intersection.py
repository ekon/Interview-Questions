# Find intersection of 2 lists of integers.

a = [1,2,6,3]
b = [4,6,1,0]

def listDiff(l1, l2):
    dup = []
    for a in l1:
        for b in l2:
            if a == b:
                dup.append(a)
    print (dup)

def setIntersection(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    print (s1 & s2)


listDiff(a,b)
setIntersection(a, b)
