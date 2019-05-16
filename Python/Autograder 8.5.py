fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
c=0
ls=[]
l=[]
l1=[]
for line in fh:
    if line.startswith('From '):
        lh=line
        l=lh.split()
        c=c+1
        print(l[1])

print("There were", c, "lines in the file with From as the first word")
