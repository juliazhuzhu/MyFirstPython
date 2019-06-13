

def partition(val_list,l,r):
    if len(val_list) <= 1:
        return
    pivotvalue=val_list[l]
    leftmark = l+1
    rightmark = r
    done = False
    while not done:
        while leftmark <= rightmark and val_list[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while val_list[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark -1
        
        if leftmark > rightmark :
            done = True
        else:
            temp = val_list[leftmark]
            val_list[leftmark] = val_list[rightmark]
            val_list[rightmark] = temp
    
    temp = val_list[l]
    val_list[l] = val_list[rightmark]
    val_list[rightmark] = temp
    return rightmark
            
        
def quick_soft(val_list,l,r):
    if l<r:
        splitpoint = partition(val_list,l,r)
        quick_soft(val_list,l,splitpoint-1)
        quick_soft(val_list,splitpoint+1,r)

val_list = [9,22,1,3,99,1000,2,44,2]

quick_soft(val_list,0,len(val_list)-1)
print(val_list)
    