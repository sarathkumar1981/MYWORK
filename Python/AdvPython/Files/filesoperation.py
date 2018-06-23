path=r'C:\Users\sarat\Documents\Python\Advpython\myfile.txt'
with open(path,'r') as fop:
    #print(fop.read())
    header = fop.readline()
    print(header)
    details=fop.readlines()
   # print(details)
    dict={}
    for i in details:
       values = i.strip().split(',')
       salary=int(values[2])
       dept=values[4]
       gen=values[3]
       key=(dept,gen)
       if (dict.get(key)==None):
           dict[key]=salary
       else:
            dict[key] = dict.get(key) +salary
    print(dict)
           
    #dict[dept].append(salary)
       #print(salary,dept)
    #print(values)
    #print("salary is %d and dept is %d"%(salary,dept))
