#!/usr/bin/env python
# coding: utf-8

# In[2]:


#PROGRAM TO CONVERT FARANHEIT TO CELSICUS
fa=float(input("enter the value:"))
ce=(0.58)*(fa-32)
print(ce)


# In[9]:


#PROGRAM TO CHECK WHETHER THE NUMNER IS  POSITIVE OR NEGATIVE
num=int(input())
if num>0:
    num=num+10
    print(num)
    print("POSITIVE")
else:
    print(num)
    print("NEGATIVE")


# In[22]:


#PROGRAM TO DETERMINE THE CHARACTER ENTERED
ch=(input())
if alpha:
        print("alphabet")
elif number:
        print("number")
elif space:
        print("space")
else:
        print("error")


# In[18]:


#WRITE A PROGRAM TO FIND A TEXT IS PRESENT IN SENTENCE ARE NOT
text=input()
if "is" in text:
    print("present")
else:
    print("not present")


# In[7]:


# WRITE A PROGRAM TO REMOVE PARTICULAR LETTER ND PRINT REMANING WORD
str="mississippi"
print(str.split("s"))
print(str.upper())
print(str.lower())
print(reversed(str))


# In[5]:


#STRING ACCESS
abc="netherlands"
print(abc[1])
print(abc[-7])


# In[24]:


#STRING SLICING//part of text
abc="netherlands"
print(abc[1:7])
print(abc[0:])
print(abc[::-1])


# In[29]:


#STRING MULTI-LINE
abc="""netherlands   
australia   
greece"""
print(abc)


# In[30]:


#STRING COMPARISION
abc="hiii"
abc1="helo"
abc2="hiii"
print(abc==abc1)
print(abc==abc2)


# In[35]:


#STRING CONCATENATION
abc="hiii  "
abc1="  helo"
abc2="  hiii"
print(abc  +  abc1 +  abc2)


# In[38]:


#method  by using sum
def lenstr(string):
    return sum(l for i in string)
string ="INDIA"
print(lenstr(string))


# In[42]:


#COUNTER METHOD
def ls(str):
    count=0
    for i in str:  #//while str[count:]
        count+=1
    return count
str="SR UNIVERSITY"
print(ls(str))


# In[19]:


#using join and count
def ls(str):
    if not str:
        return 0
    else:
        random_str="py"
        return ((random_str).join(str).count(random_str)+1)
str="INDIA"
print(ls(str))
print(str.upper())
print(str.lower())
print(str.partition())#---returns a tuple
print(str.find(2))#---it returns the index value of first substring
print(str.replace(i))#---replacing the substring
split()#--splitting the word
startswith()#---check wheather the string is starting with samewords or not
endswith()#---check wheather the string is ending with samewords or not
index()#---indexing the values


# In[53]:


#FORMATING STRINGS
name="yagna"
country="INDIA"
print(f"{name} belongs to  {country}")


# In[56]:


#SETS
m_set={1,2,3,4,2}#it doesnot consider duplicate elements
m_set1={2.0,(1,2,3,5),"yagna"}
print(m_set)
print(m_set1)


# In[57]:


x={}
print(type(x))
y=set()
print(type(y))


# In[78]:


#MODIFYING A SET
m_set={1,9}
print(m_set)
m_set.add(5)#adding
print(m_set)
m_set.update([2,3,4])#updating
print(m_set)
#ADDING OF LIST AND SET
m_set.update([6,7,8],{1,2,3})
print(m_set)


# In[82]:


m_set=set("happyday")
print(m_set)
print(m_set.pop())
print(m_set)


# In[94]:


N=10
k=int(input("Enter number"))
m=n-k+1:
    if k==0:
        print("INVALID")
        available=k+5
    elif k>0 and k<10:
        no.of_candies==k
        print(k)
    else:
        return


# In[95]:


#A digital machine generates binary data which consists of a string of 0s and 1s.A maximum signal M in the data,
#consists of maximum number of either 1s or 0s appearing consecutively in the data but M can't be at the 
#begining or end of the string. Design a way to find the length of the maximum signal.
#input
#the first line of the input consists of an integer N,representing the length of the binary string.
#the second line consists of a string of length N consists of 0s and 1s only
#input
#6
#101000
#output
#1
#input
#9
#101111110
#output
#6


# In[97]:


size=int(input())
max=0
count=0
flag=0
str=input()
arr=list(str)
for i in range(0,size):
    if arr[i]=='1':
        count=count+1
        flag=1
    elif(arr[i]=='0' and flag==1):
        count=0
        flag=0
    if count>max:
        max=count
print(max)


# In[4]:


#reverse of number using while loop recursion
n=int(input("Enter a number"))
while(n!=0):
    temp=n%10
    print(temp,end=" ")
    n=n//10


# # FOR LOOP

# In[10]:


n=int(input("Enetr number:"))
for i in range(1,n):
    print(i)


# In[11]:


n=int(input("Enter the number:"))
avg=0.0
sum=0
for i in range(1,n+1):
    sum=sum+i
avg=sum/i
print("Sum =",sum)
print("Average=",avg)


# In[13]:


#multiplication table
n=int(input("Enter the number:"))
for i in range(1,11):
    print(n,"X",i,"=",n*i)


# In[14]:


n=int(input("Enter the number:"))
for i in range(1,11):
    print(n,"+",i,"=",n+i)


# In[16]:


#printing of leap years
for i in range(1900,2101):
    if i%4==0:
        print(i,end="\t")


# In[35]:


n=int(input("Enter nth number:"))
s=0.0
for i in range(1,n+1):
    a=1.0/i
    s=s+a
print("sum of 1,1/2......1/",+str(n)+"is"+str(s))


# In[45]:


n=int(input("Enter nth number:"))
s=0.0
for i in range(1,n+1):
    a=1/(i**2)
    s=s+a
print("sum of series 1,1/2...1/"+str(n)+"is"+str(s))


# In[1]:


str="hiii"
print(str.capitalize())


# In[7]:


#   $$$$hii$$$$
str="hiiii"
print(str.center(10,"$"))


# In[11]:


str="hello"
substr="hellohellohellohellohell"
print(substr.count(str,0,len(substr)))


# In[12]:


str="hello"
print(str.lower())


# In[13]:


str="hello"
print(str.upper())


# In[21]:


str="she is my cousin"
print(str.find("is",0,len(str)))


# In[23]:


#syntax for left justification
#ljust(width[,fillchar])
str="hiiii"
print(str.ljust(20,'^'))


# In[24]:


#syntax for right justification
#rjust(width[,fillchar])
str="hiiii"
print(str.rjust(20,'^'))


# In[26]:


#syntax for zfill(width)
str="18"
print(str.zfill(4))


# In[28]:


print(ord("A"))


# In[29]:


print(ord("Z"))


# In[30]:


print(ord("a"))


# In[67]:


print(ord("n"))


# In[33]:


str="zebra"
print(max(str))


# In[36]:


str="zebra"
print(ord(max(str)))


# In[37]:


print(ord("z"))


# In[38]:


str="hello world"
print(str.title())


# In[42]:


str="Hello World"
print(str.title())
print(str.swapcase())


# In[46]:


str="hello world"
print(list(enumerate(str)))


# In[53]:


str="INDIA HAS WON"
for i in str:
    print(i,end=" ")


# In[61]:


str="INDIA HAS WON"
for i in str:
    print(i,end="   ")


# # caeser cipher

# In[54]:


str="INDIA"
index=0
while index <len(str):
    letter=str[index]
    print(chr(ord(letter)+1),end=" ")
    index+=1


# In[57]:


str="INDIA"
index=0
while index <len(str):
    letter=str[index]
    print(chr(ord(letter)-1),end=" ")
    index+=1


# In[59]:


str="INDIA"
index=0
while index <len(str):
    letter=str[index]
    print(chr(ord(letter)+2),end=" ")
    index+=1


# In[60]:


print(ord("@"))


# # ABECEDARIAN SERIES

# In[6]:


str="ate"
list=['A','B','C','D','E','F']
for letter in list:
    print(letter+str,end="\n")


# In[167]:


n=int(input("Enter the position of number:"))
a=b=0
for i in range(1,n+1):
    if(i%2!=0):
        a=a+7
    else:
        b=b+6
if n%2!=0:
    print("{} at accordance {}".format(n,a-7))
else:
    print("{} at accordance {}".format(n,b-6))


# In[201]:


n=int(input("Enter the position of number:"))
a=b=1
for i in range(0,n-1):
    if(i%2!=1):
        a=a*2
    else:
        b=b*3
if n%2!=0:
    print("{} at accordance {}".format(n,a))
else:
    print("{} at accordance {}".format(n,b))


# In[282]:


n=int(input("Enter the position of number:"))
a=b=1
for i in range(0,n+1):
    if(i%2==1):
        a=7*i
    else:
        b=6*i
if n%2!=0:
    print("{} at accordance {}".format(n,a-7))
else:
    print("{} at accordance {}".format(n,b-6))


# In[ ]:




