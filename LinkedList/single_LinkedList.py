
import os
from typing import TypeVar


node=TypeVar("node",bound="Node") # declaring type of Node class
class Node:
    def __init__(self,data:int=None) -> None:
        self.data=data
        self.next=None # to store the next node address

    def set_data(self,data:int)-> None:
        self.data=data
        
    def set_next(self,next: node)-> None:
        self.next=next
    
    def get_data(self)-> int:
        return self.data
        
    def get_next(self)-> node:
        return self.next

    
class SingleLinkedList:
    def __init__(self) -> None:
        self.head:node=None # stores the  address of beginning  node 
        self.length=0

    def node_exist(self,index: int)-> node| None: # return node if found else null
        count=0
        tmp:node=self.head # temporary object

        while(tmp!=None):
            if(count==index):

                return tmp
            tmp=tmp.get_next()
            count+=1
        return tmp # will store none if node not exist or head is none

    def get_last_node(self)-> node:
       
        tmp:node=self.head
        while(self.head!=None and tmp.get_next()!=None):
            tmp=tmp.get_next()
        return tmp

    def appendnode(self,nd:node)-> None:
        self.length+=1 # one size is increased
        if(self.head==None): # if list is empty
            self.head=nd
            return 
        tmp:node=self.get_last_node() # last node
        tmp.set_next(nd)
        print("node appended !!!!!!!!!!!!")
    
    def preappendnode(self,nd:node)-> None: # at beginning 
        self.length+=1 # one size is increased
        if(self.head==None):
            head=nd
            return
        nd.set_next(self.head) # now linking this new head with old head
        
        self.head=nd # new head

        print("node preappended !!!!!!!!!!!")

    def insert_node_after_index(self,index: int ,node_to_insert: node)-> None:
        # index start from 0 
        # if node with index not exist 
        if(index>=self.length or index<=-1):
            print(f"no node exist with index   : {index} ") 
            return 
        
        tmp:node=self.node_exist(index) # will contain the node corresponding to the given index
        
        if(tmp==None):
            print("no node exist!!!!")
            return
        node_to_insert.set_next(tmp.get_next()) # linking the node with next node
        tmp.set_next(node_to_insert) # now this node is linked with its previous node

        self.length+=1 # as size increases
        print("inserted !!!!!!!!!!!!!")

    def delete_NodeAt(self,index:int):
        if(self.head==None):
            print("list is empty!!!!!!!!!!!!!")
            return 
        
        # if node does not exist
        if(index>=self.length or index<=-1):
            print(f"no node exist with index   : {index} ") 
            return 
        if(index==0): # if we have to delete first node 
            self.head=self.head.get_next() 
            return
         
        current_node: node= self.node_exist(index)
        count=0
        prev_node:node =self.head # will store the previous node 
        while(count!=index-1 and prev_node!=None ):
            count+=1
            prev_node=prev_node.get_next()

        prev_node.set_next(current_node.get_next())

        print("node deleted!!!!!!!!!")
        self.length-=1

    def update(self,index,value)-> None:
        if(self.head==None):
            print("list is empty!!!!!!!!!!!!!")
            return 
        
        if(index>=self.length or index<=-1):
            print(f"no node exist with index   : {index} ") 
            return 

        node_to_update: node=self.node_exist(index) 
        node_to_update.set_data(value)
        print("updated!!!!!!!!!!!!!!!")

    def print(self)-> None:
        if(self.head==None):
            print("list is empty!!!!!!!!!!!!!")
            return 
        
        print("[ ",end="")
        tmp:node=self.head
        while(tmp!=None):
            print(f"{tmp.get_data()},->",end="")   
            tmp=tmp.get_next()
        print(" None]")


if __name__=="__main__" :
    s=SingleLinkedList()
    
    
    
    choice=True
    while(choice):
        print("linked list operations : ")
        print("1. appendnode()")
        print("2. preappendnode()")
        print("3. insertAfterIndex()")
        print("4. delete()")
        print("5. update()")
        print("6. print()")
        print("7. clear screen()")
        print("8. exit ()")
        choice=int(input("enter choice : "))
        if(choice==8):
            break
        node=Node()
        if(choice==7):
            os.system("cls")

        elif(choice==1):
            node.set_data(int(input("enter data: ")))
            s.appendnode(node)
        elif(choice==2):
            node.set_data(int(input("enter data: ")))
            s.preappendnode(node)
        elif(choice==3):
            index=int(input("enter node index after which u want to insert: ") )
            node.set_data(int(input("enter data: ")))
            s.insert_node_after_index(index,node)
            #s.insert_node_after_index(int(input("enter node index after which u want to insert: ") ) , node.set_data(int(input("enter data: "))))

        elif(choice==4):
            s.delete_NodeAt(int(input("enter index: ")))
        
        elif(choice==5):
            s.update(int(input("enter index: ")),int(input("new value:  ")))
        elif(choice==6):
            s.print()
        
    
            



            







        
        



        

            




        




    



   