#!/usr/bin/python
# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self,val,p=0):
        self.data = val
        self.next = p

class LinkList(object):
    def __init__(self):
        self.head = 0

    def initlist(self,data):
        self.head = Node(data[0])
        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):
        p =  self.head
        length = 0
        while p!=0:
            length+=1
            p = p.next
        return length

    def append(self,item):
        q = Node(item)
        if self.head ==0:
            self.head = q
        else:
            p = self.head
            while p.next!=0:
                p = p.next
            p.next = q

    def insert(self,index,item):
        if index ==0:
            q = Node(item,self.head)
            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p

    def delete(self,index):
        if index ==0:
            q = Node(item,self.head)
            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            post.next = p.next

l = LinkList()
l.initlist([1,2,3,4,5])
l.append(6)
l.insert(4,40)
p = l.head
print p.data
while p.next != 0:
    p=p.next
    print p.data
