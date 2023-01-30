#!/usr/bin/env python
# coding: utf-8

# In[6]:


#program to access a calss variable using class object
class abc:
    var=22
obj=abc()
print(obj.var)


# In[7]:


##program to access a class variable using class object and using 2 variables
class abc:
    var=22
    var1=30
obj=abc()
print(obj.var)
print(obj.var1)


# In[8]:


#program to access a class member using class object
class abc:
    var=22
    def display(self):
        print("this is a class method ")
obj=abc()
print(obj.var)
obj.display()


# In[9]:


##program to access a class member using class object and using 2 variables
class abc:
    var=22
    var1=30
    def display(self):
        print("this is a class method ")
obj=abc()
print(obj.var)
print(obj.var1)
obj.display()


# In[15]:


#progarm to find the constructors
#whenever value is initiated to object then it is a constructor
#__init__().....method//double underscoreinitdoubleunderscore()
#self object is always default only
#if we give dot operator then it access the value
class abc:
    def __init__(self,val):
        print("in class method")
        self.val=val
        print("the value is:",val)
obj=abc(10)


# In[19]:


#progarm to find the constructors
#whenever value is initiated to object then it is a constructor
#__init__().....method//double underscoreinitdoubleunderscore()
#self object is always default only
#if we give dot operator then it access the value
class abc:
    def __init__(self,val):
        print("in class method")
        self.val=val
        print("the value is:",val)
    def __init__(self,val1):
        self.val1=val1
        print("the value is:",val1)
obj=abc(10)
obj1=abc(20)


# In[16]:


##program to differentiate between calss and object variable
class abc():
    class_var=0   #class variable
    def __init__(self,var):
        abc.class_var+=1
        self.var=var      #object variable
        print("the object variable is",var)
        print("the class value of c-=var",abc.class_var)
obj1=abc(10)
obj2=abc(20)
obj3=abc(30)


# In[34]:


##program to illustrate a modification on numerics
class Number:
    even=0 #default val
    def check(self,num):
        if num%2==0:
            self.even=1
    def even_odd(self,num):
        self.check(num)
        if self.even==1:
            print(num,"is even")
        else:
            print(num,"is odd")
obj=Number()
obj.even_odd(3)
obj.even_odd(14)
obj.even_odd(47)
obj.even_odd(18)


# In[37]:


##program to illustrate a modification on numerics
class Number:
    evens=[] 
    odds=[]
    def __init__(self,num):
        self.num=num
        if num%2==0:
            Number.evens.append(num)
        else:
            Number.odds.append(num)
n=Number(10)
n1=Number(3)
n2=Number(14)
n3=Number(47)
n4=Number(18)
print("Even numbers are",Number.evens)
print("Odd number are",Number.odds)


# In[38]:


#delete method----c++/java analogus to destructors
#general syntax__del__
class abc():
    class_var =0
    def __init__(self,var):
        abc.class_var+=1
        self.var=var
        print("the object value is",var)
        print("the class value",abc.class_var)
    def __del__(self):
        abc.class_var-=1
        print("the object with value %d is going out of scope",self.var)
obj=abc(10)
obj1=abc(18)
obj2=abc(5)
obj3=abc(20)
obj4=abc(14)
del obj
del obj1
del obj2
del obj3
del obj4


# In[39]:


##__repr__-----syntax of the object
##__cmp__-----comparision of 2 class objects
##__len__-----builtin method which calculte the length of a object
##__call__-----its acts like a funtion to call its instances
##__lt__,__le__,__eq__,__ne__,__gt__,__ge__,----to compare 2 objects based on its instances
##__iter__-----iteration over an object
##__getitem__-----used for indexing
## general syntax of getitem
    ##def__getitem__(self,var/key)
##__setitem__-----used for assing an item in the index value
##general syntax of setitem
    ##def__steitem__(self,var/key)


# In[45]:


#program to demonstrate get and set item in a list
class numbers:
    def __init__(self,mylist):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index]=val
numlist=numbers([1,2,3,4,5,6,7,8,9])
#print(numlist[3])
print(numlist.mylist)
numlist[3]=10
print(numlist.mylist)
#print(numlist[3])


# In[46]:


#program to demonstrate get and set item in a list
class numbers:
    def __init__(self,mylist):
        self.mylist=mylist
    def __getitem__(self,index):
        return self.mylist[index]
    def __setitem__(self,index,val):
        self.mylist[index]=val
numlist=numbers([1,2,3,4,5,6,7,8,9])
print(numlist[3])
print(numlist.mylist)
numlist[3]=10
print(numlist.mylist)
print(numlist[3])


# In[11]:


class abc():
    def __init__(self,name,var):
        self.name=name
        self.var=var
    def __repr__(self):
        return repr(self.var)
    def __len__(self):
        return len(self.name)
    def __cmp__(self,obj):
        return self.var - obj.var
obj=abc("yagnasri",5)
print("the value stored in obj is",repr(obj))
print("the length of the name stored in object",len(obj))
obj1=abc("yagna",10)
val=obj.__cmp__(obj1)
if val==0:
    print("both values are equal")
elif val==-1:
    print("1st value is less than second")
else:
    print("2nd value is less than 1st")


# In[19]:


##is for illustrating use of a private method
class abc():
    def __init__(self,var):
        self.__var=var
    def __display(self):
        print("this is from class method,var=",self.__var)
obj=abc(10)
obj._abc__display()


# In[21]:


##to call a class method from another method of same class
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("var is=",self.var)
    def add_2(self):
        self.var+=2
        self.display()
obj=abc(10)
obj.add_2()


# In[22]:


## program to show how a class method which calls a function
##which means defined in the global name space
def scale_10(x):
    return x*10
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("variable is=",self.var)
    def modify(self):
        self.var=scale_10(self.var)
obj=abc(20)
obj.display()
obj.modify()
obj.display()


# In[23]:


##built-in attributes
## for get set and delete
## 1..hasattr(obj,name)-checks obj possesses the attributes values or not
## 2..getattr(obj,name,[default])
## 3..setattr(obj,name,value)---which is used to set an attribute of the object
## 4..delattr(obj,name)


# In[36]:


#program to demo builtin
class abc():
    def __init__(self,var):
        self.var=var
    def display(self):
        print("val is",self.var)
obj=abc(20)
obj.display()
print("check wheather obj has attribute var ?",hasattr(obj,"var"))
getattr(obj,"var")
setattr(obj,"var",50)
print("after setting value,var is",obj.var)
setattr(obj,"count",300)
print("new variable count is created and its value=",obj.count)
delattr(obj,"var")
setattr(obj,"var",60)
print("after deleting the attribute,var is:",obj.var)


# In[37]:


'''#built-in class attributes
1.  .__dict__
2.  .__doc__  which is specified in the object
3.  .__name__ name of the module in which a class is defined
4.  .__bases__ used for inheritances to return the base class in order '''


# In[42]:


class abc():
    def __init__(self,var1,var2):
        self.var1=var1
        self.var2=var2
    def display(self):
        print("var1 is =",self.var1)
        print("var2 is =",self.var2)
obj=abc(10,12.54)
obj.display()
print("object.__dict__-",obj.__dict__)
print("object.__doc__-",obj.__doc__)
print("object.__name__-",abc.__name__)
print("object.__module__-",obj.__module__)
print("object.__bases__-",abc.__bases__)


# In[ ]:


## garbage collections

