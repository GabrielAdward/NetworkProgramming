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



#fråga johannes varför man får bort 0an genom att ge bägge a och b 1

def fibonacci_generator() :
        a , b = 1 , 1
        while True:
            yield a
            a , b = b , a + b

fib = fibonacci_generator() 

for i in fib :
        if i > 1000000 :
            break
        else :
            print( 'Generated:' , i )
