#!/usr/bin/env python
# coding: utf-8

# ### 11. Factorial of a number

# In[15]:


def factorial(x):
    if x < 0:
        return 0
    elif x == 0 or x == 1:
        return 1
    else:
        f = 1
        while(x > 1):
            f*=x
            x -= 1
        return f

number = int(input ("Enter any number to find it's factorial: "));
print ("Factorial of ", number, " is", factorial(number))


# In[ ]:





# ### 12. Prime or Composite Number

# In[3]:


num = int(input("Enter any number: "))
if num > 1:
    for a in range(2, num):
        if (num % a) == 0:
            print ("The entered number is not a prime number")
            break
    else:
        print("The entered number is a prime number")
elif num == 0 or 1:
    print ("The entered number is neither prime nor composite number")
else:
    print("The entered number is a composite number.")


# In[ ]:





# ### 13. Palindrome or not
# 
# A string is said to be palindrome if the reverse of the string is the same as string

# In[7]:


string = input("Enter a string: ")

if string == string[:: -1]:
    print("This is a palindrome string")
else:
    print("This is not a palindrome string")


# In[ ]:





# ### 14. Third side of right-angled triangle from two given sides

# In[5]:


def pythagoras (base, height, hypotenuse):
    if base == str("b"):
        return ("Base = " + str(((hypotenuse**2) - (height**2))**0.5))
    elif height == str("b"):
        return ("Height = " + str(((hypotenuse**2) - (base**2))**0.5))
    elif hypotenuse == str("b"):
        return ("Hypotenuse = " + str(((base**2) + (height**2)**0.5)))
    else:
        return "Final Answer!"
    
print (pythagoras(4,3,'b'))
print (pythagoras(4,'b',5))
print (pythagoras('b',3,5))
print (pythagoras(4,3,5))


# In[ ]:





# ### 15. Frequency of each of the characters present in a string 

# In[9]:


string = input("Enter an string: ")

all_freq = {}

for a in string:
    if a in all_freq:
        all_freq[a] += 1
    else:
        all_freq[a] = 1
print('Count of all character in ' + string + str(all_freq))


# In[ ]:




