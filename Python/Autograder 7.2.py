# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count =0
s =0
a=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count=count+1
    pos=line.find('0')
    snum=line[pos-1:]
    num=float(snum)
    s=s+num
a=s/count
print("Average spam confidence:",a)
