large = None
small = None

while True :
    c = input("Enter Number : ")
    try:
        n=int(c)
        if large is None or small is None:
            large=n
            small=n
        elif small>n:
            small=n
        elif large<n:
            large=n
    except:
        print("Invalid input")
        if c=='Done':
        	break
print("Maximum is",large)
print("Minimum is",small)
