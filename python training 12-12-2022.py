#!/usr/bin/env python
# coding: utf-8

# In[8]:


#wheather number is happy or not
def happy(num):
    rem=0
    sum=0
    while(num>0):
        rem=num%10
        sum=sum+(rem*rem)
        num=num//10
    return sum
num=97
result=num
while(result!=1 and result!=4):
    result=happy(result)
    if result == 1:
        print("happy number")
    else:
        print("not a happy number")


# In[10]:


#find maximum of 4 digit to the base 17(10-A,11-B,12-C,13-D....16-G)as input,output is decimal value.
num=str(input())
print(int(num,17))  


# In[7]:


#greatest of two numbers
a=10
b=12
c=53
print(max(a,b,c))


# In[5]:


#wheather given number is harshed number/niven's or not.
n=int(input("Enter a number"))
sum=0
rem=0
temp=n
while(temp>0):
    rem=temp%10
    sum=sum+rem
    temp=temp//10
print("sum=",sum)
if n%sum==0:
    print("harshed/nivens Number")
else:
    print("not harshed/nivens Number")


# In[6]:


#while loop
i=0
while(i<=15):
    print(i)
    i+=1


# In[7]:


#while loop
i=15
while(i>=0):
    print(i)
    i-=1


# In[1]:


num=1234
n_string=str(num)
r_num="".join(reversed(n_string))
print("reversed number is: "+r_num)


# In[2]:


#reverse of a string using recursion
def reverse(n):
    if len(n)==0:
        return n
    return reverse(n[1:]) +n[0]
num=1234
n_string=str(num)
r_num=reverse(n_string)
print("reversed number is:"+r_num)

