def delete(i,temp_dict):
    for j in temp_dict[i]: 
        delete(j,temp_dict)
        del temp_dict[j]
    return temp_dict

n=7
A=[-1,1,1,1,3,3,4,4]
m=3
B=[2,3,4]

count=0

temp_dict={}
temp_dict.update({i:[] for i in range(1,n+1)})
deleted_node=[0 for i in range(7)]
for i in B:
    deleted_node[i-1]=1

for i in range(n,1,-1):
    if not temp_dict.get(A[i], None):
        temp_dict[A[i]] =[]
    temp_dict[A[i]].append(i)
    
B.sort()
for i in B:
    if temp_dict.get(i, None) is None:
        continue
    temp_dict=delete(i,temp_dict)
    del temp_dict[i]
    count+=1
print count
