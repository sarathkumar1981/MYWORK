with open('myfile1.txt','r') as fob1:
    t1=fob1.readlines()
     
with open('myfile2.txt','r') as fob2:
    head=fob2.readline()
    t2 = fob2.readlines()

t3 = t1 + ['\n'] + t2
with open('myfile3.txt','w') as fob3:
    
    for line in t3:
        fob3.write(line)








