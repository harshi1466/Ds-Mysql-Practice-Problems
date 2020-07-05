import math

def check(x,y,h,k,a,b):

    ##(x-h)^2/a^2 + (y-k)^2/b^2 <= 1

    point = ((math.pow((x - h), 2) // math.pow(a, 2)) + (math.pow((y - k), 2) // math.pow(b, 2))) 

    if (point > 1): 
        print ("Outside") 
  
    elif (point == 1): 
        print("On ellipse") 
  
    else: 
        print("Inside") 




h = 0
k = 0
x = 2
y = 2
a = 6
b = 5
check(x,y,h,k,a,b)
  
    