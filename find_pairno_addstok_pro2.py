n,k=input().split(" ")
n=int(n)
k=int(k)
list_num=[int(x) for x in input().split(" ")]
flag=0
for i in range(0,n):
  temp=list_num[i]
  sum=0
  for j in range(i+1,n):
    sum=temp
    sum=sum+list_num[j]
    if(sum==k):
      print("yes")
      flag=1
      break
if(flag==0):
  print("no")
