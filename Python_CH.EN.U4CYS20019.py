

import re

def writetofile(allips,filename):
    with open(filename, 'w+') as f:
        for ips in allips:
            f.write('{},{},{},{}\n'.format(ips[0],ips[1],ips[2],ips[3]))
    f.close()

def printfromfile(filename):
    f = open('conversion.txt', 'r')
    print(f.read())
    f.close()
   

regex = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def check(IP):
	if(re.search(regex, IP)):
	    print("Valid IP Address")
	else:
		print("Invalid IP Address")
		exit()

if __name__ == '__main__' :
    
    allips=[]
    
    for x in range(1,11):
        IP=input("\nEnter IPV4 Address=")
        check(IP)
        parts = IP.split('.')
       
        hex2='0x'
        for part in parts:
            hex2 += format(int(part),'02x')
            
        ipdec=0
        ipdec=int(hex2, base=16)
       
        binaryNumber = \
           format(int(parts[0]),   '08b') \
           + format(int(parts[1]), '08b') \
           + format(int(parts[2]), '08b') \
           + format(int(parts[3]), '08b')
        
        ipbin='0b'+binaryNumber
       
        oc='0o'
        for part in parts:
            oc += format(int(part),'03o')
        
        
        lt=[ipdec,ipbin,oc,hex2]
        print(lt)
        allips.append(lt)
    writetofile(allips,'conversion.txt')
    print("\nOutput from conversion.txt")
    print("\nIP address in Decimal,Binary,Octal,Hexadecimal")
    print("\n")
    printfromfile('conversion.txt')



    
    
            
