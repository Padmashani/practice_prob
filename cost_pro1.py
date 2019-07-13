inp=input().split(" ")
str_1=inp[0]
str_2=inp[1]
cost=0
len_diff=abs(len(str_1)-len(str_2))
cost+=len_diff
for i in range(0,len(str_1)):
  if (i<len(str_2)):
    if str_1[i]!=str_2[i]:
      cost+=1

print(cost)
