#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Boss:
    def __init__(self,name,attitude,behavior,rating):
        self.name=name
        self.attitude=attitude
        self.behavior=behavior
        self.rating=rating
    def getName(self):
        return self.name
    def getAttitude(self):
        return self.attitude
    def getBehavior(self):
        return self.behavior
    def getRating(self):
        return self.rating
    
class GoodBoss:
    def __init__(self,name,attitude,behavior,rating):
        self.goodBoss=Boss(name,attitude,behavior,rating)
    def getName(self):
        return self.goodBoss.getName()
    def getAttitude(self):
        return self.goodBoss.getAttitude()
    def getBehavior(self):
        return self.goodBoss.getBehavior()
    def getRating(self):
        return self.goodBoss.getRating()
    def leadbyExample(self):
        print("With",self.goodBoss.getName(),"leading, employees put their talents to good use.")
    def encourage(self):
        print("With",self.goodBoss.getName(),", employees feel happy, positive, and supported.")

class BadBoss:
    def __init__(self,name,attitude,behavior,rating):
        self.badBoss=Boss(name,attitude,behavior,rating)
    def getName(self):
        return self.badBoss.getName()
    def getAttitude(self):
        return self.badBoss.getAttitude()
    def getBehavior(self):
        return self.badBoss.getBehavior()
    def getRating(self):
        return self.badBoss.getRating()
    def blameOthers(self):
        print("The employees feel resentment and anger")
    def yell(self):
        print("Everyone stares while",self.badBoss.getName(),"yell.")


# In[ ]:




