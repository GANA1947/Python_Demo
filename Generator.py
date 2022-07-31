'''
l=range(10)
def get():
    for x in l:
        return x*x
obj=get()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

'''


def decr(f):
    def new_fun():
        print('Say Hello')
        f()
        print('Say Hai')
    return new_fun
@decr
def get():
    print('Done My Job')
get=get()


        

        
