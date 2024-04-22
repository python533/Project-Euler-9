olay=False

for i in range(1,1000):
    for b in range(1, 1000):
        c = 1000 - i - b
        if c*c ==  i*i +b*b:
            print(i*b*c)
            print(i,b,c)
            olay=True
            break
            if olay:break




