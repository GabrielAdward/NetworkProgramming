def myTest():
    yield 1
    yield 5
    yield 6
    yield 99


a = myTest()
b = myTest()
# print( a.__next__() )
# print( a.__next__() )
# print( b.__next__() )
# print( b.__next__() )
# print( a.__next__() )




def fibonacci() :
        a , b = 1 , 1
        while True:
            yield a
            a , b = b , a + b

fib = fibonacci() 

for i in fib :
        if i > 1000000 :
            break
        else :
            print( 'Generated:' , i )
