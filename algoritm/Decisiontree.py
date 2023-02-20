import numpy as np
import copy
import random
import pandas as pd
from collections import Counter
from sklearn.model_selection import train_test_split
from sklearn.utils import resample

df = pd.read_excel(r'algoritm\Valladata.xlsx')
print(df)
data = df.dropna(axis='columns')
print(data)


train, test = train_test_split(data, test_size = 0.2, shuffle = True)

def find_split_point(data, label, parameter):


    sorted_data = data.sort_values(by=parameter)
    sorted_label = sorted_data[label]
    
   
    
    gini_value = 0
    
    
    l = len(sorted_label)

    for indx in range(len(sorted_label)):

        v1 = sorted_label.head(indx).mean()
        v2 = sorted_label.tail(l-indx).mean()
       
        s1 = (v1**2) + ((1 - v1)**2)
        s2 = (v2**2) + ((1 - v2)**2)
        
        g = ((indx/l)*s1) + (((l-indx)/l)*s2) 

        if g > gini_value:
            gini_value = g
            if indx >= l-1: 
                split_value = sorted_data[parameter].values[indx]  
            else:
                split_value = (sorted_data[parameter].values[indx]+sorted_data[parameter].values[indx+1])/2
            index = indx
 
    df_head = sorted_data.head(index)
    df_tail = sorted_data.tail(l-index)
        
    return split_value, gini_value, df_head, df_tail

class TreeNode():
    def __init__(self, classification=None):
        self.split_value = None # the splitting value (c)
        self.split_parameter = None # what feature where uesd for the split (x_i)
        self.child_nodes = [] # list that contains two child nodes, if not leaf_node
        self.leaf_node = 0 # is this leaf_node (0= no, 1=yes)
        self.classification = classification # classification made in this node.
        
    def predict(self, data):
        # TODO: we need to traverse the tree recursivly down to a leaf node.
        # step 1: check if this is a leaf node, if it is then return classification otherwise contine with step 2.
        # step 2: check the input data for the splitting criteria, i.e. data[x_i] < c ...
        # (data[x_i] < c would corresponds to child_node[0] and data[x_i] => c to child_node[1])
        # step 3: call the predict function in the corresponding child_node and return the prediction. 
        if self.leaf_node:
            return self.classification
        else:

            if data[self.split_parameter] < self.split_value:
                return(self.child_nodes[0].predict(data))
            elif data[self.split_parameter] >= self.split_value:
                return(self.child_nodes[1].predict(data))

            
            
    def learn(self, data, label, min_node_size):


        i = 0
        if len(data) < min_node_size: 
            self.leaf_node = 1
            return self
        elif len(data[label].value_counts()) == 1:
            self.leaf_node = 1
            return self

        split_value = 0
        gini_val = 0
        df_head =[]
        df_tail = []
        split_param = ""
    
        for para in data.columns:
            if para != 'copium':
                s, g, dh, dt =find_split_point(data,label,para)
                if g > gini_val:
                    split_value = s
                    gini_val = g
                    df_head = dh
                    df_tail = dt
                    split_param = para
        
        self.split_value = split_value
        self.split_parameter = split_param 

        
        class_tail = round(df_tail[label].mean())
        class_head = round(df_head[label].mean())
        

        ch_0 = TreeNode(class_head).learn(df_head, label, min_node_size)
        ch_1 = TreeNode(class_tail).learn(df_tail, label, min_node_size) 

        self.child_nodes.append(ch_0)
        self.child_nodes.append(ch_1)

        return self
    
tree = TreeNode() 
tree.learn(train, data.labels, min_node_size=10)
