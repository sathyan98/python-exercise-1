d1 = {1:10,2:20}
d2 = {3:30,4:40}
d3 = {}
for d in (d1,d2):
    d3.update(d)
print(d3)













#Sample Dictionary :
#dic1={1:10, 2:20}
#dic2={3:30, 4:40}
#dic3={5:50,6:60}
#Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}