import collections
import math
import random 
import zlib
import sys

with open(r"C:\Users\gabri\OneDrive\Dokument\GitHub\NetworkProgramming\Project\LaborationNine\exempeltext.txt", "r") as file:
    data = file.read()
    print(len(data))
    byteArr = bytearray(data,'UTF-8')
    print(len(byteArr))
    



def firstHistogram (data):
    histogram = [0]*256
    histogram = collections.Counter(data)
    return histogram

def secondHistogram(bytearray):#data
    histogramTwo=[0]*256
    for char in bytearray :
        histogramTwo[char]+=1
    return histogramTwo


def makeProb(histogram):
    totalOccurences=0
    for i in range(len(histogram)):
        totalOccurences+=histogram[i]
    probHistogram=[0]*len(histogram)
    for index in range(len(histogram)):
        probHistogram[index] = round(histogram[index]/(totalOccurences),4)
    return probHistogram

def checkProbForHistogram(probHistogram):
    sum = 0
    for i in range(len(probHistogram)):
        sum+=round(probHistogram[i],4)
    return sum


def getEntropi(probHistogram):
    sum =0
    for i in range(len(probHistogram)):
        if(probHistogram[i]==0):
            continue
        else :
            sum += probHistogram[i] * math.log2(1/probHistogram[i])
    return sum 


def zipCompress(data):
    theCopy = bytearray(data,'UTF-8')
    random.shuffle(theCopy)
    code = zlib.compress(theCopy)
    print("length of code", len(code))
    codeEntropi=getEntropi(makeProb(secondHistogram(code)))
    print(codeEntropi)

    zipOrgBytearray=zlib.compress(byteArr)
    print("length of zipped bytearr", len(zipOrgBytearray))
    orgByteArrEntropi=getEntropi(makeProb(secondHistogram(zipOrgBytearray)))
    print(orgByteArrEntropi)


def testZip():
    t1 = """I hope this lab never ends because
            it is so incredibly thrilling!"""
    
    t10 = 10*t1
    print("Length of t1 = ",len(t1))
    zippedT1=zlib.compress(bytearray(t1,'UTF-8'))
    print("Length of t1 zipped = ", len(zippedT1))
    zippedT10=zlib.compress(bytearray(t10,'UTF-8'))
    print("Length of t10=", len(t10))
    print("Length of t10 zipped = ", len(zippedT10))

"""
ZIP SHUFFLED BYTEARRAY
- How long is the zip-code measured in bytes?: 
  Answer: 19833 bytes
- How long is it measured in bits?: 19833 * 8 =  bits
- Entropy : 7.971104359606428 bits/symbol

ZIP BYTEARRAY
- How long is the bytearr measured in bytes? :12848 bytes
- How long is it measured in bits?: 12848 * 8 = 102 784 bits
- Entropy : 7.974306162390387 bits/symbol

BYTEARRAY(ORIGINAL)
- Entropy: 4.593366739405364

Smallest entropy: 
the orignal bytearray have the smallest entropy.
Zipping result in removal of redundancy and better randomness.
A better entropi indicates a better randomness.
"""

  
a = firstHistogram(data)
print("CHECK HISTOGRAM")
print(a)
print()
print("HISTOGRAM")

histo= secondHistogram(byteArr)
print(histo)
print("PROB HISTOGRAM")
print()
prob = makeProb(histo)
print(prob)
sum = checkProbForHistogram(prob)
print("CHECK SUM")
print(round(sum,2))
entropy = getEntropi(prob)
print("ENRTOPY")
print(entropy)
zipCompress(data)
testZip()
