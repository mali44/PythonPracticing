#That returns a list that contains only the elements that are common between the lists;
#Program works on two lists of different sizes
#Take two lists, say for example these two:

 # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
 # and our c will be like this ;
 # c = [1, 2, 3, 5, 8, 13]
  


#list inputs from user
a = [int(i) for i in raw_input("ilk seri icin giriniz").split()]
b = [int(i) for i in raw_input("for second list").split()]
c = []
for x,y   in zip(a,b):
 if x == y:
  c.append(x)
 print (c)

#To generate randomly list
#Use this
#import random
#a=random.sample(range(20),4)
#b=random.sample(range(10),7)






