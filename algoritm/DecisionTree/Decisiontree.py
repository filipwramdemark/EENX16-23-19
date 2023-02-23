import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle
from joblib import load, dump
import graphics as gp
data = pd.read_csv('algoritm/Valladata_prep.csv')
data = data.dropna(axis='columns')                      #Getting the data format
# print(data) 
train, test = train_test_split(data, test_size = 0.2, shuffle = True) #splitting the data into training data
# train = data




class Classification_eval(object):
    def __init__(self):
        # counters 
        self.TP = 0 # correctly identified positive 
        self.FP = 0 # falsely identified positive 
        self.TN = 0 # correctly identified negative 
        self.FN = 0 # falsely identified negative 
    
    def update(self, pred, label):
        """
        pred - is the prediction will be either a 1 or 0. 
        label - is the correct answer, will be either a 1 or 0.
        """
        # TODO: add to one of the counters each time this function is called. 
        if pred == label:
            self.TP += pred 
            self.TN += (1-pred)
                
        else:
            self.FP += pred
            self.FN += (1-pred)


    
    def accuracy(self): 
        # returns the accuracy 
        if (self.TP + self.TN) == 0:
            return 0
        # TODO: calculate the accuracy.
        accuracy = (self.TP + self.TN) / (self.TP + self.TN + self.FP + self.FN)
        return np.round(accuracy, 4)
    
    def precision(self): # percentage of the estimated positive that actually is positive
        if self.TP == 0:
            return 0
        # TODO: calculate the precision.
        precision = (self.TP)/(self.TP + self.FP)
        return np.round(precision, 4)
    
    def recall(self): # percentage of correctly identified positive of the total positive
        if self.TP == 0:
            return 0
        # TODO: calculate the recall.
        recall = self.TP/(self.TP + self.FN)
        return np.round(recall, 4)


def find_split_point(data, label, parameter):
  
    # beging by sorting the data after the paramter. 
    sorted_data = data.sort_values(by=parameter)
    sorted_label = sorted_data[label]
    

    
    gini_value = 0
    
    
    l = len(sorted_label)

    for indx in range(len(sorted_label)):
        # print(indx)
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


        

   
    
    
    # TODO: get the two data frames the corresponds to the split data. 
    # the functions .head(split_index) and .tail(split_index) could be useful. 
 
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
                print(self.split_value)
                return(self.child_nodes[0].predict(data))
        
            elif data[self.split_parameter] >= self.split_value:
                print(self.split_value)
                return(self.child_nodes[1].predict(data))
    def countnodes(self):
        if self.leaf_node:
            return(1)
        return(self.child_nodes[0].countnodes() + self.child_nodes[1].countnodes())


            
    def print_childs(self, win, wid, hei):
        if self.leaf_node:
            leafp1 = gp.Point(wid*2,950-hei)
            leafp1 = gp.Point(0,950-hei+50)
            leaf = gp.Rectangle(leafp1, leafp1)
            leaf.setFill('green')
            leaf.draw(win)
            return self
        if self.child_nodes[0]:
            ch1p1 = gp.Point(wid/2,950-hei)
            ch1p2 = gp.Point(0,950-hei+50)
            ch1 = gp.Rectangle(ch1p1, ch1p2)
            ch1.setFill('blue')
            ch1.draw(win)
        
        if self.child_nodes[1]:

            ch2p1 = gp.Point((wid -(wid/2)),950-hei)
            ch2p2 = gp.Point(wid,950-hei+50)
            ch2 = gp.Rectangle(ch2p1, ch2p2)
            ch2.setFill('red')
            ch2.draw(win)
        
        return  (self.child_nodes[0].print_childs(win, (wid/2), (hei-50)) and (self.child_nodes[1].print_childs(win, (wid/2), (hei-50))))
        

    def learn(self, data, label, min_node_size):
      
        # TODO: wirte the learning function. 
        # Step 1: check if the data fullfils the min_node_size criteria, if so make this node a leaf node and return.
        # Step 1.5: Check if the data is homogenious i.e. only contains one type for the labels, if thats 
        # the case then make this node a leaf node and return.
        # print(len(data))
        # print(data.shape[0])
        
        # print(sensor_properties)
        i = 0
        if len(data) < min_node_size: 
            self.leaf_node = 1
            return self
        elif len(data[label].value_counts()) == 1:
            self.leaf_node = 1
            return self
        # for a in range(len(label)-1):
        #     if label[a] == label[a+1]:
        #         i +=1
        # if i == len(label-1):
        #     self.leaf_node = 1
        #     return

        
        split_value = 0
        gini_val = 0
        df_head =[]
        df_tail = []
        split_param = ""
        # Step 2: Loop over all features and get the best gini and split_value for each feature. 
        # Step 2.5: Save the best split value and split_paramter and the two new data frames 
        # corresponding to the split [df_head, df_tail] (these will be data frames for the child nodes). 
        for para in data.columns:
            if para != 'Valla (Label)':
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
        
        # Step 4: append the the child node to the self.child_nodes. It should be in the order 
        # of the child node correspoinding to [df_head, df_tail].

        self.child_nodes.append(ch_0)
        self.child_nodes.append(ch_1)

        return self
    
tree = TreeNode() # create root node
tree.learn(train, "Valla (Label)", min_node_size=10)

pickle.dump(tree, open('algoritm/DecisionTree/Decision_Tree.pickle', "wb"))
