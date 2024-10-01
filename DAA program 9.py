arr =[-9,3,4,6,8,9,10,30]
key=10
left=0
right=len(arr)-1
found=False
while left<=right:
    mid=left+(right-left)//2
    if arr[mid]==key:
        print(f"element {key} is found at position {mid}")
        found=True
        break
    elif arr[mid]<key:
        left=mid+1
    else:
        right=mid-1
if not found:
    print(f"element {key} is not found in the array")
