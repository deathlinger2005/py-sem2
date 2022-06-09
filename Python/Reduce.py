import functools
import Reduce as r1

l = [1,2,3,4,5,6,7,8,9,10]
a = r1(lambda x,y: x+y,l)
print(a)