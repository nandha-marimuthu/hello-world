def rem_dup(str):
    x=""
    for i in str:
        if i not in x:
            x+=i
    return(x)
