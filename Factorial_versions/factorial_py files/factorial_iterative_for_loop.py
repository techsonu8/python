#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# this is simple code to find a factorial of a number
while(1) :
    
    number = int(input("Enter a number to find its Factorial : "))

    if number < 0 :
        print("Factorial of a Negative number does not exist")
    else :
        factorial = 1
        for i in range(1,number+1):
            factorial = factorial * i
        print("Factorial of ",number, " is : ",factorial)


# In[ ]:




