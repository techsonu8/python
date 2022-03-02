#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import math 
while(1) :
    
    number = int(input("Enter a number to find its Factorial : "))

    if number < 0 :
        print("Factorial of a Negative number does not exist")
    else :
        factorial = math.factorial(number)
        print("Factorial of ",number, " is : ",factorial)


# In[ ]:




