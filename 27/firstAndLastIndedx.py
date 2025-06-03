arr=[2,4,5,5,5,5,5,7,9,9]
target=10
n=len(arr)

def FirstAndLastIdx(arr,target,n):
    for i in range(n):
        if arr[i]==target:
            start=i
            while i+1<n and arr[i+1]==target:
                i+=1
            return [start,i]
    return [-1,-1]

print(FirstAndLastIdx(arr,target,n))        
