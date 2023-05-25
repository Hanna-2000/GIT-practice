#!/usr/bin/env python
# coding: utf-8

# In[2]:


class Apple():
    def type(self):
        print("Fruit")
    def color(self):
        print("Red")
        
class Carrot():
    def type(self):
        print("Vegitable")
    def color(self):
        print("Orange")
        
obj_1=Apple()
obj_2=Carrot()

for item in (obj_1, obj_2):
    item.type()
    item.color()
        


# In[ ]:




