#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# this is simple code to find a factorial of a number
while(True):      
    number = int(input("Enter a number to find its Factorial : "))
    if number < 0 :
        print("Enter another input")
        print("Factorial of a Negative number does not exist")
    else:
        result = fact(number)
        print("Factorial of ",number, " is : ",result)
    
def fact(number) :
    if (number == 0 or number == 1) :
        return 1
    else :
        return (number * fact(number-1))


# In[ ]:




