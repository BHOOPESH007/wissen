def finding_subarray(A, n):
    result=[]
    sum_list=[]
    total_sum=sum(A)
    for i in range(n):
        sum_list.append(sum(A[:i+1]))
    sum_list.append(0)
    count=0
    i=0
    
    while i<n:
        j=i
        while j<n:
            subarray_sum=sum_list[j]- sum_list[i-1]

            subarray_len=len(A[i:j+1])
            cur_avg=float(subarray_sum)/subarray_len
            
            if len(A[0:i]+A[j+1:])==0:
                raimaning_avg=0
            else:
                raimaning_avg=float(total_sum-subarray_sum)/(n-subarray_len)
            
            if cur_avg>raimaning_avg:
                result.append([i+1, j+1])
                count+=1
            j+=1        
        i+=1
    return result, count
# n=input()
# A= map(int, raw_input().split(' '))
A=[3,4,2]
n=3
result, count = finding_subarray(A,n)

print count
for one in result:
    print one[0], one[1]
