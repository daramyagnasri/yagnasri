#!/usr/bin/env python
# coding: utf-8

# In[9]:


n=int(input("Enter size"))
if(n<=0):
    print("Invalid Input")
    exit()
else:
    l=input("Enter numbers:")
    x=l.split(" ")
    odd=[]
    even=[]
    f=[]
    fl=[]
    for i in range(0,n):
        fl.append(int(x[i]))
    fl.sort()
    for i in range(0,n):
        if(fl[i]%2==0):
            print(fl[i])
        else:
            if(fl[i]%2==0):
                e.append(fl[i])
            else:
                o.append(fl[i])
f=e+o
for i in range(n):
    print(f[i],end=" ")


# In[16]:


keys=["name","age","branch"]
values=["yagna",20,"CSE"]
outsource=zip(keys,values)
abc=dict(outsource)
print(abc)


# In[36]:


#write a program to store a sparse matrix to a dictonary
#sparse matrix=non zero elements positions and key values
matrix=[[0,0,0,1,0],
         [2,0,0,0,3],
         [0,0,0,4,0]]
dict={}
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        #print(matrix[i][j],end=" ")
        if matrix[i][j]!=0:
            dict[(i,j)]=matrix[i][j]
#print("\n")
print(dict)


# In[48]:


#print a non-repeated character in a string
#example:i/p:"level"          o/p:v
string=input()
for i in string:
    count=0
    for j in string:
        if i==j:
            count+=1
        if count>1:
            break
    if count==1:
        print(i,end=" ")


# In[60]:


#write a program to insert delete a node in a single linked list
class node:
    def __init__(self,num):
        self.num=num
        self.next=None
class llist:
    def __init__(self):
        self.head=None
    def push(self,newnum):
        newnode=node(newnum)
        newnode.next=self.head
        self.head=newnode
        def insertnext(self,previousnode,newnode):
            if previousnode is none:
                print("the previous node")
                return
            newnode=node(newnum)
            newnode.next=previousnode.next
            previousnode.next=newnode
        def append(self,newnum):
            newnode=node(newnum)
            if self.head is none:
                self.head=newnode
                return
            last=self.head
            while(last.next):
                last=laast.next
            last.next=newnode
        def printnum(self):
            t=self.head
            while(t):
                print(t.data)
                t=temp.next
if __name__=="__main__":
    ll=llist()
    ll.append(10)
    ll.append(18)
    ll.append(24)
    ll.append(5)
    ll.append(82)
    ll.append(76)
print(printnum)


# In[ ]:





# In[ ]:





# In[ ]:




