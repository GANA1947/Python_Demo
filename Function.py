''' def Normal(c,d):
    return c+d
print(Normal(10,20))

def Default(a,b=20):
    return(a+b)
print(Default(80))

def unlimited(*arg):
    return arg
print(unlimited(10))
print(unlimited(10,20))
print(unlimited(10,20,30))

def Keyword(**B):
    return B
print(Keyword(x=10))
print(Keyword(x=10,y=20))
print(Keyword(x=10,y=20,z=30))
'''
# Built in Functions
# Lambda
# Range and X range
# Iterater and Generator
# Decorater

# Lanbda: It is anonymous function, can take any number of arguments, but can only have one expression.

f = lambda x:x*x
print (f(10))

# Range and X range: Builtin functons in Python, It return list of sequence of Intergers. It will allocate the memory for all the elements.




