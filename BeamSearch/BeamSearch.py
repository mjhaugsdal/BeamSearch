#!/usr/bin/python
# CSC 547 Artificial Intelligence
# Lecturer: Sung Shin
# 
# Date: 6/17/2017
# Author: Markus Haugsdal
#
# Resources used: https://www.tutorialspoint.com/python/index.htm
#                 http://openbookproject.net/thinkcs/python/english3e/trees.html
#
# Homework 2 
# Due date: 6-21
#
#
# This is an implementation of the Beam Search Algorithm, using the test data from figure 4.2 in the class notes.


import Queue
import copy
from collections import deque

iterator = 1

# Class tree. 
# Has Cargo(Letter), Weight, Left and Right children.

class Tree:
    def __init__(self, cargo, weight = None ,left=None, right=None):
        self.weight = weight
        self.cargo = cargo
        self.left  = left
        self.right = right

    def __str__(self):
        return str(self.cargo)

 
# Builds the tree based on figure 4.2 / 4.1
# (Messy)

def make_tree():

        

    t = Tree("S", 0 , Tree("A", 3, Tree("B",4, Tree("C", 4), Tree("E", 5, Tree("D", 2), Tree("F", 4, Tree("G",3)))),
    Tree("D", 5, Tree("E",2, Tree("B",5, Tree("C",4)), Tree("F",4, Tree("G",3))))), Tree("D",4, Tree("A",5, Tree("B",4, Tree("C",4),
    Tree("E",5, Tree("F",4, Tree("G",3))))), Tree("E",2, Tree("B",5, Tree("A",4), Tree("C",4)), Tree("F",4, Tree("G",3)))))

    return t

# Simplified tree printing function
#
def print_tree(q):
    
    print("The following nodes were selected")
    while q.qsize() !=0 :
        t = q.get()
        #print(q.qsize())
        print(t.cargo)
    
# Sorting algorithm.
# Converts queue to list, then sorts the list and creates a new queue with that list
# Also used to check if goal has been reached.
# Inputs: Queue, goalQueue
# Output: Sorted queue
def sort(q,gq):
   
    global iterator
    goalNode = "G"
    
    q2 = Queue.Queue()
    l = list(q.queue)

    l.sort(key=lambda x:x.weight)

    
    print("---------------------------------------")
    print()
    print("Iteration # ", iterator)
    iterator+=1
    i = 0


    
    for tree in l:
         
         
         if tree.cargo == goalNode:
            print("Goal found! Success!") 
            gq.put(tree)
            print_tree(gq) 
         else:
            print("From ",tree.cargo) 

    
    if(q.qsize()>=2):
        for i in range (0,2):
            print("Chose ", l[i].cargo)
            q2.put(l[i])
    print("---------------------------------------")
    return q2


# Beam search function. 
# Input: Queue with root node of tree
# Output: Void

def beam_search(q):

    print("---------------------------------------")
    t = make_tree()    
    goalNode = "G"
    goalQueue = Queue.Queue()

    #Enter root into a queue
    q.put(t)
    t = q.get()
    if t.right != None:
        q.put(t.right)            
    if t.left != None:
        q.put(t.left)

    #While there are elements in the queue
    while q.qsize() != 0:
       
        #print ("Hill climb")

        if t.cargo == goalNode:
            
                      
            print_tree(goalQueue)
            
            break;
        else:
            #Remove first and second element from the queueand sort the children. Enter at the BACK of the queue.

            #Sort!

            t = q.get()
            goalQueue.put(t)

            if t.right != None:
                q.put(t.right) 
            if t.left != None:
                q.put(t.left)
            
            # Repeat for second node
            t = q.get()
            goalQueue.put(t)
       
            if t.right != None:
                q.put(t.right) 
            if t.left != None:
                q.put(t.left)

            
            q = sort(q,goalQueue)

# Main runtime
def main():

    q = Queue.Queue()
    beam_search(q)

main()