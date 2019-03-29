
def softNumbers(*args,type="asc"):
    list_args = list(args)
    if type == "asc":
        list_args.sort()
    else:
        list_args.sort(reverse=True)
    
    return list_args
        

print(softNumbers(1,4,2,2))
print(softNumbers(1,4,2,2,type="dec"))