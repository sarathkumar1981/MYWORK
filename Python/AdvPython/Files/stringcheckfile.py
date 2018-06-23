with open('filecore.txt','w') as fob:
    print("please enter the text\n")
    str= None
    while (str!='@'):
        str = input()

        if (str !='@'):
            fob.write(str + '\n')

    #print(fob.read())