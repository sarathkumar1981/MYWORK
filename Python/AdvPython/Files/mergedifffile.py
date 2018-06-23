with open('myfile1.txt','r') as f1:
    file1_content = f1.readlines()

with open('myfile2.txt','r') as f2:
    h1 = f2.readline()
    file2_content = f2.readlines()

file2_new = []
for line in file2_content:
    words = line.split(',')
    id = words[0]
    name=words[2]
    salary=words[1]
    gen = words[3]
    dept = words[4].split('\n')[0]
    rec = id+','+ name +','+ salary + ',' + gen + ',' + dept +'\n'
    file2_new.append(rec)
 
file3_content = file1_content+['\n']+file2_new

with open('file_new.txt','w') as fnew:
    for line in file3_content:
        fnew.write(line)

