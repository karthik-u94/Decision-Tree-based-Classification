#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from collections import Counter

from operator import itemgetter

import time
import copy
import sys


# In[2]:


class Images:
    def __init__(self, LabelVector):
#     self.label = label
#     self.vector = vector
        self.LabelVector=LabelVector
    def __getitem__(self,index):
        return self.LabelVector[index]

    
# 


# In[3]:


class DTreeNode:
    def __init(id,splitIndex,spltValue,leftChild,rightChild,label):
        self.id=id
        self.splitIndex=splitIndex
        self.splitValue=splitValue
        self.leftChild=leftChild
        self.rightChild=rightChild
        self.label=label
    


# In[4]:


class DecisionTreeNode:
    def __init(self,label,vector,nodeId,leftChild,rightChild):
        self.label=label
        self.vector=vector
        self.nodeId=nodeId
        self.leftChild=leftChild
        self.rightChild=rightChild
    


# In[5]:


# filename="data/rep1/train.csv"
# minfreq=20
# modelfile="dtreemodelfull20.csv"

filename=str(sys.argv[1])
minfreq=int(sys.argv[2])
modelfile=str(sys.argv[3])

ImageList=[]




with open(filename, 'r') as f:
    reader = csv.reader(f)
    data = list(list(rec) for rec in csv.reader(f, delimiter=',')) 
    
for image in data:
    img= Images(LabelVector=None)
    img.LabelVector=[float(i) for i in image]
    ImageList.append(img)
    
# ImageList=ImageList[:500]

NodeUsageList=[False]*(len(ImageList[0].LabelVector)-1)


# In[6]:


def GetSplit(classLabels, attr):
    BestSplitPoint=0
    MinIndex=0
    MinGini=2
    NodeSize=len(attr)
#     SplitPoints=[float(attr[0])-1]
    SplitPoints=[]
    for  i in range(0, len(attr)):

         if(i!=len(attr)-1):
            SplitPoints.append(float(attr[i]+float(attr[i+1]))/2)
    
    ClassDistribution = [[0 for x in range(2)] for y in range(10)] 
    
    for i in range(10):
        ClassDistribution[i][1]=classLabels.count(i)
        
    for i in range(1, len(attr)):
        gini=0

        if((i!=0 and attr[i-1]!=attr[i]) or i==0):
        
            ClassDistribution[int(classLabels[i])][0]+=1
            ClassDistribution[int(classLabels[i])][1]-=1
            gini=GetGiniIndex(ClassDistribution,NodeSize)
            if(gini<MinGini):
                MinGini=gini
                BestSplitPoint=SplitPoints[i-1]
                
    
                
    
    
    return BestSplitPoint,MinGini
            
        
        

        
    


# In[7]:


def GetGiniIndex(ClassDistr,N):
    GiniTotal=0
    left=[x[0] for x in ClassDistr]
    right=[x[1] for x in ClassDistr]
    Nleft=sum(left)
    Nright=sum(right)
    
    GiniSumL=0
    GiniSumR=0
    
    for i in range(0,10):
        if(Nleft!=0):
            GiniSumL+=(left[i]/Nleft)**2
        if(Nright!=0):
            GiniSumR+=(right[i]/Nright)**2
    
    Gini=(Nleft/N*(1-GiniSumL))+(Nright/N*(1-GiniSumR))
    
    return Gini
        
    
    


# In[8]:


def isPure(LabelList):
    isPure=True
    UniqueLabels=list(set(LabelList))
    if(len(UniqueLabels)>1):
        isPure=False
        return isPure
    return isPure


# In[9]:


def MinCountSatisfied(NodeSize, MinSize):
    if(NodeSize>Minsize):
        return True
    return False
    


# In[10]:


def isNodeUsed(index):
    if(NodeUsageList[index]==True):
        return True
    return False


# In[11]:


DTree=[]
NodeIndex=0
splits=0
def ConstructDTree(ImageList, NodeUsage):
    global NodeIndex
    MinGiniIndex=2
    BestSplitPoint=0
    BestSplitIndex=0
    VectorMatrix=[img.LabelVector for img in ImageList]
    BestLeft=[]
    BestRight=[]
    global splits
    
    
# Check if node needs to be split

    if(isPure(x[0] for x in ImageList) or len(NodeUsage)==len(VectorMatrix[0])-1 or len(ImageList)<minfreq):
#         NodeIndex+=1
        LeafNode=DTreeNode()
        LeafNode.id=NodeIndex
        LeafNode.leftChild=None
        LeafNode.rightChild=None
        LeafNode.splitIndex=None
        LeafNode.splitValue=None
        
        if(isPure(x[0] for x in ImageList)):
            LeafNode.label=ImageList[0].LabelVector[0]
        else:
            lblList=[x[0] for x in ImageList]
            LeafNode.label=max(lblList,key=lblList.count)
#         print(LeafNode.splitIndex)
        DTree.append(LeafNode)
    else:
#     Get best split

        for i in range(1,len(VectorMatrix[0])):
            if(i-1 not in NodeUsage):
            
                SortedList=sorted(VectorMatrix,key=itemgetter(i))
                attributes=[x[i] for x in SortedList]
                classLabels=[x[0] for x in SortedList]
            
                SplitPoint,Gini=GetSplit(classLabels,attributes)
            
                if(Gini<MinGiniIndex):
                    MinGiniIndex=Gini
                    BestSplitIndex=i-1
                    BestSplitPoint=SplitPoint
                    
    
#         print("Best split pt: "+str(BestSplitPoint)+" at "+str(BestSplitIndex)+" gini "+str(MinGiniIndex))
        splits+=1
        
#         print(splits)
        NewNodeUsage=copy.deepcopy(NodeUsage)
        NewNodeUsage.append(BestSplitIndex)
#         print(NewNodeUsage)
        BestLeft=[img for img in ImageList if float(img[BestSplitIndex+1]) <= BestSplitPoint]            
        BestRight=[img for img in ImageList if float(img[BestSplitIndex+1]) > BestSplitPoint]
        

        NewNode=DTreeNode()
        NewNode.id=NodeIndex
        NewNode.label=None
        NewNode.splitIndex=BestSplitIndex
        NewNode.splitValue=BestSplitPoint
        if(len(BestLeft)>0):
            NodeIndex+=1
            NewNode.leftChild=NodeIndex
            ConstructDTree(BestLeft,NewNodeUsage)
        else:
            NewNode.leftChild=None
        if(len(BestRight)>0):
            NodeIndex+=1
            NewNode.rightChild=NodeIndex
            ConstructDTree(BestRight,NewNodeUsage)
        else:
            NewNode.rightChild=None
#         print(NewNode.splitIndex)
        DTree.append(NewNode)
#         print(NodeUsageList)
    
    
    


# In[12]:


start=time.time()
ConstructDTree(ImageList,[])
end=time.time()
ex=end-start
#print("Time: " +str(ex))


# In[ ]:





# In[ ]:


DTree.sort(key=lambda x:x.id)


# In[ ]:


with open(modelfile, mode='w') as op:
    modelWriter = csv.writer(op, delimiter=',')
    for node in DTree:
        modelWriter.writerow([node.id,node.label,node.splitIndex,node.splitValue,node.leftChild,node.rightChild])
    


# In[ ]:





# In[ ]:




