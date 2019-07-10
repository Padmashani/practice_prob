def compute_xor(sub_list):
    xor_val=sub_list[0]
    for i in range(1,len(sub_list)):
        xor_val=xor_val+(xor_val^ sub_list[i])
    print(xor_val)

inp1=input().split(" ")
n=int(inp1[0])
q=int(inp1[0])
list_num=input().split(" ")
list_num=[int(x) for x in list_num]
for i in range(0,q):
    inp=input().split(" ")
    u=int(inp[0])
    v=int(inp[1])
    sub_list = list_num[u - 1:v]
    compute_xor(sub_list)
