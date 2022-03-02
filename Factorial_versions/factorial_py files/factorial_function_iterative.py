#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# a function is created

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
    factorial = 1
    for i in range(1,number+1):
        factorial = factorial * i
    return factorial


# In[ ]:




