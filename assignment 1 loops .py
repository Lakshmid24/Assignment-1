#!/usr/bin/env python
# coding: utf-8

# In[26]:


#WAP TO GET FIBONACCI SERIES BETWEEN 0 AND 50
n1,n2=0,1
count=1
while count<=50:
    print(count,end=' ')
    n1=n2
    n2=count
    count=n1+n2


# In[37]:


#WAP TO ACCEPT A WORD FROM THE USER AND REVERSE IT
str=input("enter a word ")
str_rev=str[::-1]
print(str_rev)


# In[36]:


#WAP TO COUNT NUMBER OF EVEN AND ODD NUMBERS FROM A SERIES OF NUMBERS
n=(1,2,3,4,5,6,7,8,9)
even=0
odd=0
for i in n :
    if i%2==0:
        even+=1
    else: 
        odd+=1
print("number of even numbers is: ", even)
print("number of odd numbers is: ", odd)

