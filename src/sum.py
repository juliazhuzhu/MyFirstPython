
def sum_val(val_list):
    if len(val_list) == 0:
        return 0
    return val_list[0] + sum_val(val_list[1:])


print(sum_val([1,2,3,4,22,1]))