# Enter your code here. Read input from STDIN. Print output to STDOUT

phoneBook = {}

n = int(input())

for i in range(0, n):
    s = input()
    sList = s.split(' ')
    phoneBook[sList[0]] = sList[1]

s = input()
while True:
    try:
        if s in phoneBook:
            txt = s + "=" + phoneBook[s]
            print(txt)
        else: 
            print("Not found")
        s = input()
    except EOFError:
        break
