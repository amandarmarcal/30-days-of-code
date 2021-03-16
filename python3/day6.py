iter = int(input())


for i in range(0, iter):
    string1 = input()
    strOdd = ''
    strEven = ''
     
    for j in range(0, len(string1)):
        
        if j%2 == 0:
            strEven+= string1[j]
        else:
            strOdd+= string1[j]
    
    print(strEven, strOdd)
