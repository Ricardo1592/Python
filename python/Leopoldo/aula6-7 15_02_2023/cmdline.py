import getopt 
import sys

first =""
last =""
args = sys.argv[1:]

try:
    options, args = getopt.getopt(argv, "f:l:", ["first =", "last ="])
except:
    print("alguma mensagem de erro")    

for name, value in options:
    if name in ['-f', '--first']:
        first=value
    elif name in ['-l', '--last']:
        last=value
        

print("Firsr: ", first)    
print("Last: ", last)    