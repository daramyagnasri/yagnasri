#!/usr/bin/env python
# coding: utf-8

# In[1]:


#while loop
i=0
while(i<=15):
    print(i)
    i+=1


# In[2]:


i=0
while(i<=31):
    print(i,end="\t")
    i+=1


# In[3]:


m=int(input())
n=int(input())
sum=0
while(m<=n):
    sum=sum+m
    m=m+1
print("sum=",sum)


# In[4]:


#sum of digits in a number and display
sum=0
m=int(input("Enter number"))
while(m!=0):
    temp=m%10
    sum=sum+temp
    m=m//10
print("sum of digits is",sum)


# In[ ]:




