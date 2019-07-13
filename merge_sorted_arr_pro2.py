n=int(input())
num_list=[]
for i in range(0,n):
  inp=[int(x) for x in input().split(" ")]
  num_list+=inp
#print(sorted(num_list))
num_list=sorted(num_list)
num_list=[str(x) for x in num_list]
print(" ".join(num_list))
