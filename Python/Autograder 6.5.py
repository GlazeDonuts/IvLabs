text = "X-DSPAM-Confidence:    0.8475";
pos=text.find('0')
numst=text[pos-1:]
number=float(numst)
print(number)
