#!/usr/bin/env python
# coding: utf-8

# In[1]:


##ABSTRACT CLASS
##iys the process of handling the information by hiding
##informal or unnecessary information for the user
class fruit:
    def taste(self):
        raise NotImplementedError()
        ##abs lacks required derived class
        ##by raising an exception
    def rich(self):
        raise NotImplementedError()
    def color(self):
        raise NotImplementedError()
class mango(fruit):
    def taste(self):
        return "sweet"
    def rich(self):
        return "vitamin A"
    def color(self):
        return "Golden yellow"
class orange(fruit):
    def taste(self):
        return "sour"
    def rich(self):
        return "vitamin c"
    def color(self):
        return "orange"
Alphanso=mango()
print(Alphanso.taste(),Alphanso.rich(),Alphanso.color())
Orange=orange()
print(Orange.taste(),Orange.rich(),Orange.color())


# In[2]:


## the attributes which are accessing the class of a class is called meta class


# In[4]:


##POLYMORPHISM(changing)
class Complex():
    def __init__(self):
        self.real=0
        self.img=0
    def setValue(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,c):
        temp=Complex()
        temp.real=self.real+c.real
        temp.img=self.img+c.img
        return temp
    def display(self):
        print("(",self.real,"+",self.img,"i)")
c1=Complex()
c1.setValue(1,5)
c2=Complex()
c2.setValue(3,9)
c3=c1+c2
print("result is....")
c3.display()

        


# In[8]:


'''##OPERATOR           FUNCTION NAME
    +                   __add__
    +=                  __iadd__
    -                   __sub__
    -=                  __isub__
    *                   __mul__
    *=                  __imul__
    /                   __truediv__
    /=                  __idiv__
    **                  __pow__
    **=                 __ipow__
    %                   __mod__
    %=                  __imod__
    >>                  __rshift__
    >>=                 __irshift__
    <<                  __lshitf__
    <<=                 __irshift__
    &                   __and__
    &=                  __iand__
    |                   __or__
    |=                  __ior__
    ^                   __xor__
    ^=                  __ixor__
    ~                   __invert__
    ~=                  __iinvert__
    >                   __gt__
    <                   __lt__
    >=                  __ge__
    <=                  __le__           '''


# In[11]:


##PROGRAM THAT HAS ABSTRACT CLASS TO DERIVE 2 CLASSES
##RECTANGLE AND TRIANGLE FROM POLYGON CLASSES
##WRITE THE METHODS TO GET DETAILS AND DIMENSIONS
##AND HENCE CALCULATE THE AREA RESPECTIVELY
class polygon:
    def get_data(self):
        raise NotImplementedError()
    def area(self):
        raise NotImplementedError()
class rectangle(polygon):
    def get_data(self):
        self.length=float(input("Enter rectangle length:"))
        self.bredth=float(input("Enter rectangle bredth:"))
    def area(self):
        return self.length*self.bredth
class triangle(polygon):
    def get_data(self):
        self.base=float(input("Enter triangle base:"))
        self.height=float(input("Enter triangle height:"))
    def area(self):
        return 0.5*self.base*self.height
R=rectangle()    
R.get_data()
print("Area of rectangle",R.area())
T=triangle()    
T.get_data()
print("Area of Triangle",T.area())


# In[12]:


##ENCAPSULATION OF PUBLIC MEMBERS
class pub:
    def __init__(self,name,num):
        self.name=name
        self.num=num
    def Num(self):
        print("roll num is",self.num)
obj=pub("yagna",1198)
obj.Num()


# In[3]:


##PROGRAM TO OVERLOAD THE __CALL__ METHOD
class multi:
    def __init__(self,num):
        self.num=num
    def __call__(self,0):
        return self.num * 0
x=multi(10)
print(x(5))


# In[6]:


##PROGRAM TO OVER-RIDE GET-ITEM ND SET-ITEM METHODS
class mylist:
    def __init__(self,List):
        self.List=List
    def __getitem__(self,index):
        return self.List[index]
    def __setitem__(self,index,num):
        self.List[index]=num
    def __len__(self):
        return len(self.List)
    def display(self):
        print(self.List)
L=mylist([1,2,3,4,5,6,7,8,9])
print("list is.....")
L.display()
index=int(input("Enter the index of the list:"))
print(L[index])
index=int(input("Enter the index of the list:"))
num=int(input("Enter the position u want to modify:"))
L[index]=num
L.display()
print("the length of list is",len(L))


# In[9]:


##SPECIAL OR MISCELLANEOUS FUNCTIONS IN OVERLOADING
class number:
    def __init__(self,num):
        self.num=num
    def display(self):
        return self.num
    def __abs__(self):
        return abs(self.num)
    def __float__(self):
        return float(self.num)
    def __hex__(self):
        return hex(self.num)
    def __oct__(self):
        return oct(self.num)
    def __setitem__(self,num):
        self.num=num
n=number(-14)
print("n is = ",n.display())
print("abs(n) is =",abs(n))
n=abs(n)
print("Converting to float",float(n))
print("Converting to hexa",hex(n))
print("Converting to octa",oct(n))


# In[7]:


##TO VISUALIZE INHERITANCE FLOW


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is ",self.name)
        print("age is ",self.age)
class teacher(person):
    def __init__(self,name,age,exp,rarea):
        person.__init__(self,name,age)
        self.exp=exp
        self.rarea=rarea
    def displaydata(self):
        person.display(self)
        print("exprience is",self.exp)
        print("reqasearch area",self.rarea)
class student(person):
    def __init__(self,name,age,course,marks):
        person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def displaydata(self):
        person.display(self)
        print("course=",self.course)
        print("marks=",self.marks)
print("---------------TEACHER CLASS----------------")
T=teacher("Marks",43,20,"JSS")
T.displaydata()
print("---------------STUDENT CLASS----------------")
S=student("yagna",20,"B.E",53)
S.displaydata()


# In[10]:


##PROGRAM TO INVOKE __INIT__ IN MULTIPLE INHERITANCE
class base1(object):
    def __init__(self):
        print("base class 1")
class base2(object):
    def __init__(self):
        print("base class 2")
class Derived(base1,base2):
    pass
D=Derived()


# In[12]:


##PROGRAM TO CALL CONSTRUCTO OF A BASE CLASS FROM SUPER(Multilevel inheritance)
class base1(object):
    def __init__(self):
        print("base class 1")
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print("base class 2")
class Derived(base1,base2):
    pass
D=Derived()


# In[14]:


##PROGRAM TO CALL CONSTRUCTO OF A BASE CLASS FROM SUPER(Multilevel inheritance)
class base1(object):
    def __init__(self):
        print("base class 1")
        super(base1,self).__init__()
class base2(object):
    def __init__(self):
        print("base class 2")
class Derived(base1,base2):
    def __init__(self):
        super(Derived,self).__init__()
        print("Derived class")
D=Derived()


# In[22]:


##TO VISUALIZE INHERITANCE FLOW
##USING ISINSTANCE AND ISSUBCLASS

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("name is ",self.name)
        print("age is ",self.age)
class teacher(person):
    def __init__(self,name,age,exp,rarea):
        person.__init__(self,name,age)
        self.exp=exp
        self.rarea=rarea
    def displaydata(self):
        person.display(self)
        print("exprience is",self.exp)
        print("reqasearch area",self.rarea)
class student(person):
    def __init__(self,name,age,course,marks):
        person.__init__(self,name,age)
        self.course=course
        self.marks=marks
    def displaydata(self):
        person.display(self)
        print("course=",self.course)
        print("marks=",self.marks)
print("---------------TEACHER CLASS----------------")
T=teacher("Marks",43,20,"JSS")
T.displaydata()
print("---------------STUDENT CLASS----------------")
S=student("yagna",20,"B.E",53)
S.displaydata()
print("T is a teacher :",isinstance(T,teacher))
print("T is a integer :",isinstance(T,int))
print("T is a object :",isinstance(T,object))
print("T is a Personr :",isinstance(T,person))
print("Person is a sub class of teacher",issubclass(person,teacher))
print("teacher is a sub class of person",issubclass(teacher,person))
print("Boolean is a subclass of int:",issubclass(bool,int))


# In[26]:


##MULTIPATH
class person:
    def name(self):
        print("name is...........")
class teacher(person):
    def qual(self):
        print("qualification is PHD")
class hod(teacher):
    def expe(self):
        print("experience is 22 yrs")
HOD=hod()
HOD.name()
HOD.qual()
HOD.expe()


# In[2]:


##multipath inheritance
class student:
    def name(self):
        print("name---------------")
class academic(student):
    def acad_score(self):
        print("academic score 90% above")
class CSE(student):
    def CSE_score(self):
        print("CSE Score--------------60% and above")
class result(academic,CSE):
    def eligibility(self):
        print("...............ELIGIBILE TO APPLY..............")
        self.acad_score()
        self.CSE_score()
R=result()
R.eligibility()


# In[ ]:




