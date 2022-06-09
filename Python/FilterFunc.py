l = []
for i in range(1,11):
    l.append(i)

print(l)
# l is a list containing numbers from 1 to 10

def even(n):
    if n % 2 == 0:
        return True
# This even function returns True for even no.s

l2 = list(filter(even,l))
print(l2)
# l2 -> list which contains filtered elements of list l(even no.s)

l3 = list(filter(lambda x: x % 2 == 0,l))
print(l3)
# l3 does same thing as l2 but we don't need another function(even) here.

l4 = list(map(lambda x: 3*x,l))
print(l4)
# l4 -> list. lambda -> returns 3* every element in list l, this is mapped into l5 by map() function.

l5 =[1,2,3,4,5,6,7,8,9,10]

l6 = list(map(lambda x,y: x+y,l,l5))
print(l6)
# l6 -> list. Adds contents of lists l and l5