n=input()
inp=input().split(" ")
inp=[int(x) for x in inp]
res=[]
for i in range(0,len(inp)):
    if inp[i]==i:
        res.append(inp[i])
res.sort()
res=[str(x) for x in res]
print(" ".join(res))
