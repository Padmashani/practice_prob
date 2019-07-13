n=int(input())
list_of_num=[]
count=0
for i in range(1,n+1):
  list_of_num.append(i)
for i in range(0,n):
  for j in range(i+1,n):
    count+=1
print(count)
