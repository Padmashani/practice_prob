n=input()
inp=input().split(" ")
inp=[int(x) for x in inp]
freq_list=[]
for num in inp:
  if freq_list.count(num)>1:
    freq_list.append(num)
freq_list=sorted(freq_list)
freq_list=[str(x) for x in freq_list]
print(" ".join(freq_list))
