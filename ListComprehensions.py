 '''
 
 Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
 Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
 
 '''
 
cool = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evenNumbers=[]

for index,numb in enumerate(cool):
     if(cool[index]%2==0):
           print(cool[index])        
           evenNumbers.append(cool[index])
           print(evenNumbers)
          



