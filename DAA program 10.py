nums=[5,2,9,1,5,6]
n=len(nums)
size=1
while size<n:
    left=0
    while left<n-size:
        mid = left+size-1
        right=min((left+2*size-1),(n-1))
        left_sub=nums[left:mid+1]
        right_sub=nums[mid+1:right+1]
        i=j=0
        k=left
        while i<len(left_sub)and j<len(right_sub):
            if left_sub[i]<=right_sub[j]:
                nums[k]=left_sub[i]
                i+=1
            else:
                nums[k]=right_sub[j]
                j+=1
            k+=1
        while i<len(left_sub):
            nums[k]=left_sub[i]
            i+=1
            k+=1
        while j<len(right_sub):
            nums[k]=right_sub[j]
            j+=1
            k+=1
        left+=2*size
    size*=2
print(nums)
