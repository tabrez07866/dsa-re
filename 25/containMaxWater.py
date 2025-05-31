#method implementation

def containMaxWater(height):
    left=0
    right=len(height)-1
    res=[]
    while(left<right):
        area=min(height[left],height[right])*(right-left)
        res.append(area)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return max(res)


#Driver Code
height=[1,8,6,2,5,4,8,3,7]
print(containMaxWater(height))
            