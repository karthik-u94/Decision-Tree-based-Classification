#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import sys

# In[2]:


class DTreeNode:
    def __init(id,splitIndex,spltValue,leftChild,rightChild,label):
#         self.id=id
        self.splitIndex=splitIndex
        self.splitValue=splitValue
        self.leftChild=leftChild
        self.rightChild=rightChild
        self.label=label


# In[3]:


# ModelFile="dtreemodelfull20.csv"
# TestFile="data/rep2/test.csv"
# PredictionFile="prediction.csv"

ModelFile=str(sys.argv[1])
TestFile=str(sys.argv[2])
PredictionFile=str(sys.argv[3])

with open(ModelFile, 'r') as f:
    reader = csv.reader(f)
    data = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

DTreeDict={}

for node in data:
    NewNode=DTreeNode()
#     NewNode.id=node[0]
    NewNode.label=float(node[1]) if node[1] is not '' else None
    NewNode.splitIndex=int(node[2]) if node[2] is not '' else None
    NewNode.splitValue=float(node[3]) if node[3] is not '' else None
    NewNode.leftChild=float(node[4]) if node[4] is not '' else None
    NewNode.rightChild=float(node[5]) if node[5] is not '' else None
#     print(node[0])
    DTreeDict[int(node[0])]=NewNode

    
Prediction=[]    

with open(TestFile, 'r') as f:
    reader = csv.reader(f)
    data = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

Images=[]
for x in data:
    lst=[float(i) for i in x]
    Images.append(lst)
    
# print(DTreeDict.get(0))


# In[4]:



for img in Images:
    predLabel=None
    nodeId=0
    node=DTreeDict.get(nodeId)
    while(predLabel==None):
        
        if(img[node.splitIndex+1]<=node.splitValue):
            nodeId=node.leftChild
            
        else:
            nodeId=node.rightChild
            
        node=DTreeDict.get(nodeId)
        predLabel=node.label
    lst=[img[0],predLabel]
    Prediction.append(lst)


# In[5]:


with open(PredictionFile, mode='w') as op:
    modelWriter = csv.writer(op, delimiter=',')
    for pred in Prediction:
        modelWriter.writerow([pred[0],pred[1]])
    


# In[ ]:





# In[ ]:




