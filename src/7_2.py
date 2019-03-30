
def binarySearch (arr, l, r, x): 
  
    # Check base case 
    if r >= l: 
  
        mid = l + int((r - l)/2)
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1
    
def bin_search(val, val_list):
    if len(val_list) == 0:
        return -1
    pos = int(len(val_list)/2)
    print(pos)
    if val_list[pos] == val:
        return pos
    
    if len(val_list) == 1:
        return -1
    
    if val > val_list[pos]:
       val_list = val_list[pos+1:]
    else:
        val_list = val_list[:pos]
    return bin_search(val, val_list)
    
vvv = [3,4,5,6,8,10,22]
vvv.sort()
print(bin_search(31,vvv))
print(bin_search(3,vvv))
print(bin_search(22,vvv))


arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x)
print(result)