import re
def testPartA ():
    txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
    
    #prints 5 or
    a = re.findall("or", txt)
    
    #prints word for word
    b = re.findall(".", txt)
    
    #gets part of words containing or
    c = re.findall( "or.", txt)
    
    #gets ['13.', 'UR.']
    d = re.findall("..\.", txt)
    #print(d)
    
    
def testPrefix():
    #Hello
    #World
    print("Hello\nWorld")  

    #Hello\nWorld
    #print(r"Hello\nWorld")
    

def otherSpecialCharacters():
   txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
   A =  re.findall(r"\w", txt) 
   
   #big W means not word character
   AB =  re.findall(r"\W", txt) 
   
   #little d stands for digits
   abc= re.findall(r"\d", txt)
   abcd =  re.findall(r"\D", txt)
   
   #The rule to remember is s as in space or s as in separator, because also line
    #break, line feed, and tabulator ('\n', '\r', '\t') count.
   bc= re.findall(r"\s", txt)
   bcb =    re.findall(r"\S", txt)


def userDefinedSets():
    txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
    t = re.findall(r"[bcdfghjklmnpqrstvxz]", txt)

def repetions():
        txt = "Hanoror bought 5 portions of orange soil for 13.50 EUR."
        bababa = re.findall(r"\d+", txt)
        baba = re.findall(r"\w+", txt)
        ababa = re.findall(r"\w*or\w*", txt)
        
        #The regex searches for a string that rst contains zero or more characters
        #that can be letters or digits and after this contains one digit.
        tytyyt = re.findall(r"\w*\d", "abc123def456ghi")
        hhshsh = re.findall(r"\w*?\d", "abc123def456ghi")
        
        #A ?-character after the star makes the algorithm lazy instead of gready. The
        #strings that match now still start as early as possible, but are not longer
        #than necessary:
        
def taskoOne():
    mtxt = "jox r.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."
    #Since we experiment, our rst try could be to nd words that contain @
    test = re.findall(r"\w+@\w\w", mtxt)
    print(test)

testPartA()
testPrefix()
otherSpecialCharacters()
userDefinedSets()
repetions()
taskoOne()

