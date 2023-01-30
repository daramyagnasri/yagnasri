#!/usr/bin/env python
# coding: utf-8

# # PATTERNS
# #BASIC PATTERNS
# 
# #MIRROR IMAGE PATTERNS
# 
# #SYMMETRICAL PATTERNS
# 
# #CHOICE OF PATTERNS
# 
#     ##CROSS PATTERNS
#     ##STEPBYSTEP PATTERNS
#     
# #ANTI PATTERNS/HALLOW PATTERNS

# In[1]:


rows=int(input("Enter no.of rows:"))
for i in range(0,rows):
    for j in range(rows):
        print("$",end=" ")
    print("\n")


# In[3]:


rows=int(input("Enter no.of rows:"))
for i in range(rows):
    for j in range(i+1):
        print("$",end=" ")
    print("\n")


# In[4]:


rows=int(input("Enter no.of rows:"))
for i in range(rows,0,-1):
    for j in range(0,rows+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("$",end=" ")
    print("\n")


# In[5]:


rows=int(input("Enter no.of rows:"))
for i in range(1,rows+1):
    for j in range(0,rows+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("$",end=" ")
    print("\n")


# In[6]:


rows=int(input("Enter no.of rows:"))
for i in range(rows,0,-1):
    for j in range(0,i):
        print("$",end=" ")
    print("\n")


# In[7]:


rows=int(input("Enter no.of rows:"))
for i in range(rows):
    for j in range(i+1):
        print(j+1,end=" ")
    print("\n")


# In[8]:


rows=int(input("Enter no.of rows:"))
for i in range(rows,0,-1):
    for j in range(0,i):
        print(j+1,end=" ")
    print("\n")


# In[9]:


rows=int(input("Enter no.of rows:"))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print(j,end=" ")
    print("\n")


# In[10]:


rows=int(input("Enter no.of rows:"))
for i in range(0,rows):
    for j in range(0,i+1):
        print("@",end=" ")
    print("\n")


# In[11]:


rows=int(input("Enter no.of rows:"))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print(j-1,end=" ")
    print("\n")


# In[12]:


rows=int(input("Enter no.of rows:"))
for i in range(rows,0,-1):
    for j in range(0,rows+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print(j-1,end=" ")
    print("\n")


# In[13]:


rows=int(input("Enter no.of rows:"))
for i in range(rows,0,-1):
    for j in range(0,i):
        print(j,end=" ")
    print("\n")


# In[14]:


rows=int(input("Enter no.of rows:"))
for i in range(1,rows+1):
    for j in range(1,rows+i):
        if(j<i):
            print(" ",end=" ")
        else:
            print("@",end=" ")
    print()


# In[15]:


rows=int(input("Enter no.of rows:"))
for i in range(rows,0,-1):
    for j in range(1,rows+i):
        if(j<i):
            print(" ",end=" ")
        else:
            print("@",end=" ")
    print()


# In[17]:


rows=int(input("Enter no.of rows:"))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if(j<i):
            print("",end=" ")
        else:
            print("@",end=" ")
    print('')


# In[17]:


#using for loop
rows=int(input("Enter no.of rows:"))
for i in range(1,rows+1):
    for j in range(1,rows+1):
        if(j<i):
            print(" ",end=" ")
        else:
            print("@",end=" ")
    print()


# In[18]:


#using while loop
rows=int(input("Enter no.of rows"))
i=1
while(i<=rows):
    j=1
    while(j<=rows):
        if(j<i):
            print(" ",end=" ")
        else:
            print("@",end=" ")
        j=j+1
    i=i+1
    print()


# In[2]:


rows=int(input("Enter no.of rows:"))
for i in range(0,rows):
    for j in range(0,i+1):
        print("INDIA",end=" ")
    print("\n")


# In[27]:


a=65
r=11
for i in range(0,r):
    for j in range(0,i+1):
        ch=chr(a)
        print(ch ,end=" ")
        a+=1
    print("")


# In[73]:


a=65
r=2
m=(2*a)-2
for i in range(0,r):
    for j in range(0,m):
        print(end= " ")
    m=m-1
    for j in range(0,i+1):
        ch=chr(a)
        print(ch, end=" ")
        a+=1
    print( " " )


# In[74]:


rows=10
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()


# In[84]:


rows=10
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(i+j,end=" ")
    print()


# # functions syntax
# def username(arg1,arg2,arg3.....n):
#     
#        -------
#        
#        -------
#        
#        return

# In[80]:


#DIFFERENCES
def difference(a,b):
    return a-b
x=100
y=50
operation=difference
print(operation(x,y))


# In[81]:


#ADDITION
def add(a,b):
    return a+b
x=100
y=50
operation=add
print(operation(x,y))


# In[96]:


#PROGRAM TO DISPLAY A STRING AN NUMBER OF TIMES
def fun():
    for i in range(5):
        print("HII HELLO HOW R U")


# In[97]:


def difference(a,b):
    result=a-b
    print("difference of a & b is",result)
a=100
b=50
difference(a,b)


# In[ ]:




