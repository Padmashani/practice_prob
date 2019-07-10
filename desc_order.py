n=input()
list_num=input().split(" ")
list_num=[int(x) for x in list_num]
list_num=sorted(list_num,reverse=True)
for num in list_num:
    print(num)
