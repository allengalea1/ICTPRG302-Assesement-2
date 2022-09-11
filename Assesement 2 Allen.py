from asyncio.base_subprocess import WriteSubprocessPipeProto
from telnetlib import ENCRYPT

print("\nPassword Manager")

username = input("/nEnter your username of your new credentials ")
password = input("/nEnter your password of your new credentials")
choice = ''
while choice != 'q':
   
    print("\n[1] Enter 1 to create an encryption key.")
    print("[2] Enter 2 to …….")
    print("[3] Enter 3 to……")
    print("[q] Enter q to quit.")
    
 
    choice = input("\nMake your choice ")

name = input ("\nWhat's your username? ")
charSet="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz`~!@#$%^&*()_-=|\}]{[\"':;?/>.<, "
enpassword = "".join([charSet[(charSet.find(c)+3)%95] for c in password])
print("\nyour encrypted name is", enpassword)

website = input("/Enter the website name ")
f = open("file.txt", "a")
f.write(username + "   " + enpassword + "   " + website)
print("/Your new details have now been stored/n")



f= open("file.txt", "r")
data = f.read()
print(data)

try:
    f = open('file.txt')  
    print("file exists")
    f.close()    
except FileNotFoundError:
    print('No password file created, create and add data to a new file first')




 
