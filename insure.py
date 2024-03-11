a=1.02
b=1000000
i=1
while i<40:
    b = b*a
    print("value=",i, str(b))
    if(i>10):
        b = b-3600*12
    i=i+1