#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import sys

# In[2]:


# PredictionsFile="predictionR.csv"

PredictionsFile=str(sys.argv[1])

with open(PredictionsFile, 'r') as f:
    reader = csv.reader(f)
    predictions = list(list(rec) for rec in csv.reader(f, delimiter=',')) 
    
# predictions[0]
# predictions[0][0]
    


# In[3]:


ConfMatrix = [[0 for x in range(10)] for y in range(10)] 

for pred in predictions:
    ConfMatrix[int(float(pred[1]))][int(float(pred[0]))]+=1
#       print(int(float(pred[1])))

#print(ConfMatrix)


# In[4]:


num=sum(ConfMatrix[i][i] for i in range(10))
denom=sum(sum(ConfMatrix[i]) for i in range(10))

Accuracy=num/denom*100
#print(num)
#print(denom)


# In[5]:


print("------------------Confusion Matrix----------------------")
for conf in ConfMatrix:
    print(conf)


# In[6]:


print("Accuracy : "+str(Accuracy)+"%")


# In[ ]:





# In[ ]:




