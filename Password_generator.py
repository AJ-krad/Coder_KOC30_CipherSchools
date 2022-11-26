import random
import string
a=input("* Name -> ")
print(">> Hello,welcome",a,'<<' )
print(" ")
s1=string.ascii_uppercase                      #include 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
s2=string.digits                               #include '0123456789'
s3=[ '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '!', '=','?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
s4=string.ascii_lowercase                      #include 'abcdefghijklmnopqrstuvwxyz'

passlen=int(input("* Enter length of password you want to generate\n-> ")) #Taking input from user to get length of password to be generated
s=[]                                           #taking an empty  list
s.extend(list(s1))      
s.extend(list(s2))
s.extend(s3)                                  #extend used to add only the elements of the list { here of s1,s2,s3,s4 in empty list s
s.extend(list(s4))
random.shuffle(s)                             #randomly shuffeling the new list element s
B="".join(s[0:passlen])
'''here we are cancatenating the elements of the randomly shuffeled
list by using "".join upto the input by user and assigning it to variable B '''

print(" ")
print('* Your generated password is','\n->',B)

print(" ")

def passcode(B):
    s1=string.ascii_uppercase
    s2=string.digits
    s3=[ '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '!', '=','?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
    s4=string.ascii_lowercase
    if len(B)<12:
        
        print("The generated password is weak")
        return
    else:
        sum=0
        
        for i in range(len(B)):
            if str(B[i]) in s1:                    #   here we are making a function named
                sum+=1
                                                    # passcode that checks the four codition to determine 
                                                    # the strength of the password
            if str(B[i]) in s2:
                sum+=1
                
            if str(B[i]) in s3:
                sum+=1
                
            if str(B[i]) in s4:
                sum+=1
                
        
        if (sum!=len(B)):
            print("The generated password is weak")
        else:
            print("The generated password is good")
passcode(B)

        
            
        
            
        
              
              
        
        
        
        
