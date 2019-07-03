inp=input().split(" ")
res=[]
for word in inp:
    res.append(word[::-1])
print(" ".join(res))
