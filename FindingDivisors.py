#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#(If you don’t know what a divisor is, it is a number that divides evenly into another number. 
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)



y=input("Give a number \n")
x=range(2,(y))

print("number is created in list") //info


for a in x:
        if (y % a) ==0 :
                print(str(a)+"is a divisor of"+str(y))






