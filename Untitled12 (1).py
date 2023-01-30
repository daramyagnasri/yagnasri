#!/usr/bin/env python
# coding: utf-8

# # ROCK,PAPER,SCISSORS GAME 

# In[5]:


from random import randint
choice=['ROCK','PAPER','SCISSORS']
pcount=0
ccount=0
limit=5
while True:
    player=input("Enter any choice:")
    computer=choice[randint(0,2)]
    print("computers choice:",computer)
    if player == computer:
        print("--DRAW MATCH--")
    elif player == "PAPER" and computer == "ROCK":
        print("**player wins the match**")
        pcount=pcount+1
    elif player == "ROCK" and computer == "SCISSORS":
        print("**player wins the match**")
        pcount=pcount+1
    elif player == "SCISSORS" and computer == "PAPER":
        print("**player wins the match**")
        pcount=pcount+1
    else:
        print("##computer wins the match##")
        ccount=ccount+1
    if pcount==limit or ccount==limit :
        break
print("COMPUTER'S COUNT=",ccount)
print("PLAYER'S COUNT",pcount)
if pcount>ccount:
    print("PALYER WONS THE GAME")
else:
    print("COMPUTER WON THE GAME")


# In[ ]:




