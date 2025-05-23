# Time complexity=O(nlogn)
# space complexity=O(n)


def merge(arr,i,mid,j):
    #n1 => Number of element in left subarray (i,mid)
    n1=mid-i+1
    #n2 => Number of element in left subarray (mid+1,j)
    #n2=j-(mid+1)+1
    n2=j-mid

    #initialization of left and right subArray
    leftSubArray=[0]*n1
    rightSubArray=[0]*n2

    #copy elements from an array to subArrays
    for m in range(n1):
        leftSubArray[m]=arr[i+m]
    
    for n in range(n2):
        rightSubArray[n]=arr[mid+1+n]
    

    #returning a sorted subArray
    p,q=0,0
    k=i
    while p<n1 and q<n2:
        if leftSubArray[p]<=rightSubArray[q]:
            arr[k]=leftSubArray[p]
            p+=1
        else:
            arr[k]=rightSubArray[q]
            q+=1
        k+=1
    while p<n1:
        arr[k]=leftSubArray[p]
        p+=1
        k+=1
    while q<n2:
        arr[k]=rightSubArray[q]
        q+=1
        k+=1



    

            

def mergeSort(arr,i,j):
    if i<j:
        #Divide
        mid=i+(j-i)//2
        #conquer
        #Recursive Call => Left subTree
        mergeSort(arr,i,mid)
        #Recursive Call => right subTree
        mergeSort(arr,mid+1,j)
        #Combine
        merge(arr,i,mid,j)
        
    return arr

    





#diver 
arr=[10,12,34,3,56,7,67,3,232,676,10,1,2,4,5]
i=0
j=len(arr)-1
result=mergeSort(arr,i,j)
print(result)