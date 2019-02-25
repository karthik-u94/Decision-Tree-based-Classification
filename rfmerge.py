#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from collections import Counter
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


# ModelFile="dtreemodelfull2.csv"
# TestFile="data/rep2/test.csv"

# PredictionFile="predictionR.csv"
TestFile=str(sys.argv[1])
PredictionFile=str(sys.argv[2])





    
Prediction=[]    

with open(TestFile, 'r') as f:
    reader = csv.reader(f)
    data = list(list(rec) for rec in csv.reader(f, delimiter=',')) 

Images=[]
for x in data:
    lst=[float(i) for i in x]
    Images.append(lst)
    
PredMatrix = [[0 for x in range(101)] for y in range(len(Images))] 
# print(len(PredMatrix))
# print(DTreeDict.get(0))


# In[4]:


for i in range(100):
    ModelFile="pred"+'{0:03}'.format(i+1)+".csv"
    DTreeDict={}
    with open(ModelFile, 'r') as f:
        reader = csv.reader(f)
        data = list(list(rec) for rec in csv.reader(f, delimiter=',')) 



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
    index=0
    for img in Images:
        predLabel=None
        nodeId=0
        node=DTreeDict.get(nodeId)
        while(predLabel==None):
        
            if(img[node.splitIndex+1]<=node.splitValue):
                nodeId=node.leftChild
#                 print("left")
            else:
                nodeId=node.rightChild
#                 print("right")
            node=DTreeDict.get(nodeId)
            predLabel=node.label
        if(i==0):
            PredMatrix[index][0]=img[0]
#         print(i+1)
        PredMatrix[index][i+1]=predLabel
        index+=1
    


# In[5]:


for pred in PredMatrix:
    PredLst=pred[1:]
#     print(len(PredLst))
    data = Counter(PredLst)
    best=max(PredLst, key=data.get)
    lst=[pred[0],best]
    Prediction.append(lst)
    


# In[6]:


with open(PredictionFile, mode='w') as op:
    modelWriter = csv.writer(op, delimiter=',')
    for pred in Prediction:
        modelWriter.writerow([pred[0],pred[1]])
    


# In[ ]:





# In[ ]:




