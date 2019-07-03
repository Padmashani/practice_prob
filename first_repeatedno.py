n=input()
inp=input().split(" ")
inp=[int(x) for x in inp]
flag=0
for no in inp:
    if inp.count(no)>=1:
        print(no)
        flag=1
        break
if(flag==0):
    print('unique')
