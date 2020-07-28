def rem_dup(arr):
    x=[]
    for i in arr:
        if i not in x:
            x.append(i)
    return(x)
