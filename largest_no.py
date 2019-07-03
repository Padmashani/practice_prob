n=input()
inp=input().split(" ")
inp=[int(x) for x in inp]
inp.sort(reverse=True)
inp=[str(x) for x in inp]
print("".join(inp))
