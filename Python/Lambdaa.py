def double(n):
    return 2*n
# double function returns double of no. provided as argument

func1 = lambda x : 2*x
a = double(4)
# func1 is a lambda function which does the same thing as double function.

b=func1(5)
print(b)

func2 = lambda x,y : x + y
# func2 is a lambda function which takes two arguments and returns their sum

c = func2(5,7)
print(c)