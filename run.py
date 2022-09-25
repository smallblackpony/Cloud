import os
from string import *
from collections import Counter
import socket   
hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname)  
path = "/home/data" 
files= os.listdir(path) 
global position  
for file in files: 
    if file.endswith(".txt"):
        position = path+'/'+ file 
        print (position) 
    
                  
file1 = open("/home/data/Limerick-3.txt", "rt")
data1 = file1.read()   
words1 = data1.split()  
file2 = open("/home/data/IF.txt", "rt") 
data2 = file2.read()   
words2 = data2.split()    
Total =  len(words1)+len(words2)
print ('Words of Limerick-3:',len(words1))
print ('Words of IF:',len(words2))
print ('Total number of words in both files:',Total)
Counter = Counter(words2)
most_occur = Counter.most_common(3)

print('Top 3 words in IF:',most_occur)

print("My IP is:"+IPAddr)   


with open("/home/output/result.txt", "w") as w:
    for file in files:
        if file.endswith(".txt"): 
            position = path+'/'+ file 
            print (position,file = w) 
    print ('Words of Limerick-3:',len(words1),file = w)
    print ('Words of IF:',len(words2),file = w)
    print ('Total number of words in both files:',Total,file = w)
    print('Top 3 words in IF:',most_occur,file = w)
    print("My IP is:"+IPAddr,file = w)   

