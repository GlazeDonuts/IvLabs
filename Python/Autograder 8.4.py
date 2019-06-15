fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    line=line.rstrip()
    split=line.split()
    for x in split:
        lst.append(x)
lst.sort()
t=0
lst1=[]
for x in lst:
    if t!=x:
        lst1.append(x)
        t=x
print(lst1)
