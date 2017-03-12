

#Ask the user for a string and print out whether this string is a palindrome or not.
#(A palindrome is a string that reads the same forwards and backwards.)

mystr1= input("Give a String")
 
fromLeft=0
fromRight=1
pointer=0 

while True:
    if fromLeft > int(len(mystr1)):
        break
    if fromRight > int(len(mystr1)):
        break
    
    checker=mystr1[fromLeft]
    fromLeft+=1
    revChecker=mystr1[-fromRight]
    fromRight+=1
    
    if (checker != revChecker):
        flag=0
        
    else:
        flag=1
           

if pointer==1:
    print(mystr1+"is a Palindrome")
else:
    print(mystr1+"not a Palindrome")        
 
