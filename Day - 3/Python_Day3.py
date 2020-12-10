#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Dictionaries
d = {'key1':'value1','key2':'value2','key3':'value3'}


# In[3]:


price_lookup = {'apple':5.9,'orange':7,'milk':100}


# In[5]:


price_lookup['milk']


# In[6]:


d = {'k1':23,'k2':[0,1,2],'k3':{'insidekey':100}}


# In[7]:


d['k3']['insidekey']


# In[8]:


d1 = {'keys1':['a','b','c']}


# In[10]:


mylist = d1['keys1']


# In[12]:


letter = mylist


# In[13]:


letter=mylist[2]


# In[14]:


letter


# In[15]:


letter.upper()


# In[16]:


d1['keys1'][2].upper()


# In[17]:


d = {'k1':100,'k2':200}


# In[18]:


d['k3']=300


# In[19]:


d


# In[20]:


d['k1']='new value'


# In[21]:


d


# In[22]:


key=[1,2,3,4,5]


# In[23]:


value=[100,200,300,400,500]


# In[24]:


data=dict(zip(key,value))


# In[25]:


data


# In[26]:


data.keys()


# In[27]:


data.values()


# In[28]:


data.items()


# In[29]:


d1={'k1':'hello','k2':'very'}


# In[30]:


d1.pop('k2')


# In[31]:


d1


# In[33]:


d2={'k':'bye','k1':'rain','k3':'good'}


# In[34]:


d2.popitem()


# In[35]:


d2


# In[ ]:


#function
#def name_of_function():
   # "function explain
    "
    #print("")


# In[41]:


def name_of_function(name):
    print("Hello" + name)


# In[42]:


name_of_function("Jose")


# In[43]:


def say_hello():
    print("hello")


# In[47]:


say_hello()


# In[48]:


def add_num(num1,num2):
    return num1+num2


# In[49]:


add_num(10,20)


# In[50]:


def print_result(a,b):
    print(a+b)


# In[51]:


def return_result(a,b):
    return a+b


# In[54]:


result = print_result(10,20)


# In[55]:


result


# In[56]:


type(result)


# In[58]:


result = return_result(10,20)


# In[59]:


result


# In[60]:


type(result)


# In[61]:


#logic with function


# In[62]:


2%2


# In[63]:


def sum_numbers(num1,num2):
    return num1+num2


# In[64]:


sum_numbers('10','20')


# In[65]:


#logic


# In[66]:


2%2


# In[67]:


3%2


# In[68]:


20%2==0


# In[69]:


21%2==0


# In[70]:


def even_check(number):
    result=number%2==0
    return result
    


# In[71]:


even_check(20)


# In[72]:


even_check(37)


# In[73]:


def even_check(number):
    return number%2==0


# In[74]:


even_check(36)


# In[80]:


#check inside the list
def check_even_list(num_list):
    for number in num_list:
        if number%2==0:
            return True
        else:
            pass #not do anything
        
        return False


# In[76]:


check_even_list([1,2,3])


# In[78]:


check_even_list([1,3,5,7])


# In[79]:


check_even_list([1,1,1,2])


# In[81]:


check_even_list([3,3,3])


# In[82]:


check_even_list([2,1,1])


# In[ ]:


#recursion


# In[94]:


def fact(n):
    if n==0:
        return 1
    return n*fact(n-1) #return 5*4
result = fact(5)
print(result)


# In[ ]:


li = list(map(int,input().split()))
print(li)


# In[ ]:




