#!/usr/bin/env python
# coding: utf-8

# In[1]:


#createing variables
class Student:
    name="yagna"
    rollno=1198
obj=Student()
print(obj.name)
print(obj.rollno)


# In[2]:


#createing variables using private
class Student:
    name="yagna"
    __rollno=1198
obj=Student()
print(obj.name)
print(obj.__rollno)


# In[5]:


#createing variables using getter method
class Student:
    name="yagna"
    __rollno=1198
    def get_rollno(self):
        return self.__rollno

obj=Student()
print(obj.name)
print(obj.get_rollno)


# In[7]:


#createing variables setter method
class Student:
    name="yagna"
    __rollno=1198
    def get_rollno(self):
        return self.__rollno
    def set_rollno(self,new_value):
        self.__rollno=new_value
obj=Student()
print(obj.name)
print(obj.get_rollno)


# In[13]:


#
class A:
    def method_1(self):
        print("class A")
class B:
    def method_1(self):
        print("class B")
class Child(A,B):
    pass
ob=Child()
print(ob.method_1)


# In[22]:


#collecting the user name and password of a person
a=int(input("Enter number of person:"))
for i in range(0,a):
    b=input("Enter name:")
    c=input("Enter pwd:")
    print(b)
    print(c)


# In[23]:


#using dictionaries
n=int(input("Enter number of persons:"))
arr=[]
for i in range(n):
    username=input("Username:")
    password=input("password:")
    arr.append({username:password})
print(arr)


# In[35]:


#check user details are correct or not
n=int(input("Enter number of persons:"))
arr=[]
for i in range(n):
    username=input("Username:")
    password=input("password:")
    arr.append({username:password})
print(arr)
check=input("username:")
check1=input("password:")
if (username==check and password==check1):
    print("valid details")
else:
    print("invalid details")


# In[36]:


#check user details are correct or not using Exception handling
n=int(input("Enter number of persons:"))
arr=[]
for i in range(n):
    username=input("Username:")
    password=input("password:")
    arr.append({username:password})
print(arr)
check=input("username:")
check1=input("password:")
found=False
for obj in arr:
    try:
        password=obj[check]
        found =True
        if check1==password:
            print("valid password")
        else:
            print("invalid password")
    except:
        pass
if found == False:
    print("User not found")


# In[42]:


#stack 
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)
stack.append(5)
print(stack)
print(stack)
stack.pop(0)
print(stack)


# In[47]:


#quees
queue=[]
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
print(queue)
#queue.enqueue(6)
print(queue)
queue.dequeue


# In[ ]:




