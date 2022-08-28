
import os
from typing import TypeVar


node=TypeVar("node",bound="Node")

class Node:
    def __init__(self)->None:
        self.data=0
        self.next:node=None
        self.prev: node=None
    
    def set_data(self,data):
        self.data=data
        
    def set_next(self,next):
        self.next=next

    def set_prev(self,prev):
        self.prev=prev

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head=None
        self.length=0


    def nodeexist(self,index: int)-> node | None:
        if(index<0 or index>=self.length):
            print("invalid index !!!!!\n ")
            return None
        tmp:node =self.head
        while(index!=0 and tmp!=None):
            index-=1
            tmp=tmp.get_next()
        return tmp # tmp will be none if node not exist or head is null else it will give the node
        # correspond to given index  

    def get_last_node(self)-> node:
        tmp:node=self.head
        while(tmp.get_next()!=None):
            tmp=tmp.get_next()
        return tmp
    
    def appendnode(self,n: node)->None:
        self.length+=1
        if(self.head==None): # first node appending
            self.head=n
        else:
            last:node=self.get_last_node() # link new node with previous lasst node
            last.set_next(n)
            n.set_prev(last)
        print("Node Appended!!!!!\n")

    def preappend(self,n:node)->None:
        self.length+=1
        if(self.head==None):
            self.head=n
        else:
            n.set_next(self.head) # new head point to previous head

            self.head.set_prev(n) # previous head point prev point to new head

            self.head=n # new head

            print("Preappended node !!!!!!!")

    def insert_after_index(self,index:int ,new_node:node)->None:
        if(self.head==None):
            print("List is empty!!!!!!!!\n")
            return None

        node_at_index:node=self.nodeexist(index) 

        if(node_at_index!=None):
            
            self.length+=1

            new_node.set_next( node_at_index.get_next() ) # new node next point to its next node

            new_node.set_prev(node_at_index) # prev of new node point to node at given index

            node_at_index.set_next(new_node) # now node at given index point to new node

            # this check is necessary as if new node is inserted after last node
            # then after this new node is null
            # i,e newnode next point to null
            if(new_node.get_next() != None): 
                (new_node.get_next()).set_prev(new_node)

            print(f"Node inserted after {index} :\n")
        
        else:
            print(f"cannot insert node after index : {index}!!!!!")

    
    def deletenodeAt(self,index:int )->None:
        if(self.head==None):
            print("list is empty!!!!!!!!!!!!!!!!!!")

        elif(index==0): # deleting the head of list
            self.head=self.head.get_next()

            # this check is necessary as if list become empty then head is null
            
            if(self.head!=None):
                self.head.set_prev(None)

            print(f"deleted node at index: {index}")

        else:
            tmp:node =self.nodeexist(index)
            
            if(tmp!=None):

                prev_node:node =tmp.get_prev()
                after_node:node=tmp.get_next()

                prev_node.set_next(after_node)

                # this check is necessary as if last node is deleted 
                # then after is null and hence must be checked
                if(after_node !=None):
                    after_node.set_prev(prev_node)
                
                self.length-=1

                print(f"deleted node at index :  {index}  ")
            else:
                print(f"cannot delete node at index : {index} ")

    def update(self,index:int,newdata:int)->None:
        if(self.head==None):
            print("list is empty!!!!!!!!!!")

    
        else:
            node_at_index : node =self.nodeexist(index)
            
            if(node_at_index!=None):
                node_at_index.set_data(newdata)
                print(f"Node Updated at index: {index} !!!!!!!!!!!")

            else:
                print(f"Node cannot be Updated at index: {index} !!!!!!!!!!!")


    def printlist(self)->None:
        if(self.head==None):
            print("list is empty!!!!!!!!!!")
        
        else:
            tmp:node=self.head
            print("elements are : None ",end="")
            while(tmp!=None):
                print(f"( <-- {tmp.get_data()} --> )",end=" ")
                tmp=tmp.get_next()
            print("None")
    

if __name__=="__main__" :
    s=DoubleLinkedList()
    
    
    
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
            s.preappend(node)
        elif(choice==3):
            index=int(input("enter node index after which u want to insert: ") )
            node.set_data(int(input("enter data: ")))
            s.insert_after_index(index,node)
            #s.insert_node_after_index(int(input("enter node index after which u want to insert: ") ) , node.set_data(int(input("enter data: "))))

        elif(choice==4):
            s.deletenodeAt(int(input("enter index: ")))
        
        elif(choice==5):
            s.update(int(input("enter index: ")),int(input("new value:  ")))
        elif(choice==6):
            s.printlist()

        else:
            print("enter proper choice!!!!!!\n\n")
        




                
            
        









        
        


