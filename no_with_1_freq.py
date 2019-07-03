n=input()
inp=input().split(" ")
inp=[int(x) for x in inp]
for no in inp:
    if inp.count(no)==1:
        print(no)
        break
