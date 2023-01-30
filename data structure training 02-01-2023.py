#!/usr/bin/env python
# coding: utf-8

# In[1]:


#program to find the number of ones present in between two zeros
size=int(input())
max=0
count=0
flag=0
str=input()
arr=list(str)
for i in range(0,size):
    if arr[i]=="1":
        count=count+1;
        flag=1
    elif(arr[i]=="0" and flag==1):
        count=0
        flag=0
    if count>max:
        max=count
print(max)


# In[5]:


v=int(input("number of vechiles:" ))
w=int(input("no.of wheels:"))
if w<=v or w<2 or w&1==1:
    print("Invalid input:")
else:
    a=((4*v)-w)//2
print("two wheeler",a)
print("four wheeler",v-a)


# In[21]:


class binarytree:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
def insert(root,newvalue):
    if root is None:
        root=binarytree(newvalue)
        return root
    if newvalue<root.data:
        root.leftchild=insert(root.leftchild,newvalue)
    else:
        root.rightchild=insert(root.rightchild,newvalue)
    return root
    
def inorder(root):
    if root == None:
        return
    inorder(root.leftchild)
    print(root.data)
    inorder(root.rightchild)
    
root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)
print("INORDER TRAVERSAL OF BINARYTREE IS:")
inorder(root)


# In[23]:


class binarytree:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
def insert(root,newvalue):
    if root is None:
        root=binarytree(newvalue)
        return root
    if newvalue<root.data:
        root.leftchild=insert(root.leftchild,newvalue)
    else:
        root.rightchild=insert(root.rightchild,newvalue)
    return root
def preorder(root):
    if root==None:
        return
    print(root.data)
    preorder(root.leftchild)
    preorder(root.rightchild)
root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)
print("PREORDER TRAVERSAL OF BINARYTREE IS:")
preorder(root)


# In[25]:


class binarytree:
    def __init__(self,data):
        self.data=data
        self.leftchild=None
        self.rightchild=None
def insert(root,newvalue):
    if root is None:
        root=binarytree(newvalue)
        return root
    if newvalue<root.data:
        root.leftchild=insert(root.leftchild,newvalue)
    else:
        root.rightchild=insert(root.rightchild,newvalue)
    return root
def postorder(root):
    if root==None:
        return
    postorder(root.leftchild)
    postorder(root.rightchild)
    print(root.data)
root=insert(None,15)
insert(root,10)
insert(root,24)
insert(root,5)
insert(root,14)
insert(root,22)
insert(root,55)
print("PREORDER TRAVERSAL OF BINARYTREE IS:")
postorder(root)


# In[33]:


#HORIZONTAL DISTANCE EVALUATION WITH HASH FUNCTION   ///META INHERITANCE IN MULTILEVEL PATH
class Node:
    def __init__(self,key,left=None,right=None):
        self.key=key
        self.left=left
        self.right=right
def vot(node,dist,d):                          ###vot-vertical order traversal
    if node is None:
        return
    d.setdefault(dist,[]).append(node.key)
    vot(node.left,dist-1,d)
    vot(node.right,dist+1,d)
def printverticalordertraversal(root):
    d={}                    ##empty set
    vot(root,0,d)
    for value in d.values():
        print(value)
if __name__=="__main__":
    root =Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.right.left=Node(4)
    root.right.right=Node(5)
    root.right.left.left=Node(6)
    root.right.left.right=Node(7)
    root.right.left.right.left=Node(8)
    root.right.left.right.right=Node(9)
    printverticalordertraversal(root)


# In[ ]:




