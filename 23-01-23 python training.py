#!/usr/bin/env python
# coding: utf-8

# In[4]:


#PROGRAM TO FIND GREATEST OF THE 3 NUMBERS USING IF CONDITION
x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
z=int(input("Enter 3rd number:"))
if x>y and x>z:
    print("x is greater")
elif y>x and y>z:
    print("y is greater")
else:
    print("z is greater")


# In[19]:


rows=int(input("Enter no.of rows:"))
for i in range(rows):
    for j in range(i+1):
        print(end=" * ")
    print("\n")


# In[20]:


rows=int(input("Enter no.of rows:"))
for i in range(rows):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")


# # FACTORIAL 

# In[29]:


x=int(input("Enter a number:"))
sum=1
for i in range(1,x+1):
    sum=sum*i
print("factorial of number is",sum)


# # FIBONACCI SERIES

# In[ ]:


x=int(input("Enter a number:"))
x1,x2=0,1
count=0


# # PRIME OR NOT

# In[ ]:


def prime(n,div=None):
    if div is None:
        div=n-1
    while div>=2:
        if n%div==0:
            print("Not a prime:")
            #return "false"
        else:
            return prime(n,div-1)
    else:
        print("number is prime")
        #return "true"
n=int(input("Enter a number:"))
prime(n)


# In[ ]:


#calculate average of the elements in a list
def Average(my_list):
    return sum(my_list) / len(my_list)
my_list = [1,5,18,27,32]
avg = Average(my_list)
print("Average of list is=",avg)


# In[21]:


#printing of a list
list=['Red','Green','White','Black','Pink','Yellow']
list = [x for (i,x) in enumerate(list) if i not in (0,4,5)]
print(list)


# In[ ]:





# In[ ]:




