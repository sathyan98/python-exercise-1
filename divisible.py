l1 = []
for i in range(1500, 2500):
    if (i%7==0) and (i%5 ==0):
        l1.append(str(i))
print(','.join(l1))