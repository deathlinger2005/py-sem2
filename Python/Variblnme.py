def sumax(*n):
    s = 0
    for x in n:
        s += x
    b = max(n)
    return s,b

a = sumax(1,2,3,4,5)
print("Sum of all arguments provided = ",a[0],"Max of all arguments = ",a[1])