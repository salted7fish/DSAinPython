from DSAinPython.LinkedList.MyError import *

#结点类
class LNode:
    def __init__(self, elem=None, next_=None):
        self.elem = elem
        self.next = next_

#单链表类
class SingleLinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def length(self):
        cur = self.head
        count = 0

        while cur != None:
            count += 1
            cur = cur.next

        return count

    #打印输出链表中所有元素
    def show(self):
        cur = self.head

        while cur != None:
            print(cur.elem)
            cur = cur.next

    #在链表头部插入元素
    def add(self, elem):
        node = LNode(elem)
        node.next = self.head
        self.head = node

    #在链表尾部插入元素
    def append(self, elem):
        node = LNode(elem)

        if self.isEmpty():
            self.head = node
        else:
            cur = self.head

            while cur.next != None:
                cur = cur.next

            cur.next = node

    #在链表任意位置插入元素
    def insert(self, elem, index):
        length = self.length()
        if index < 0 or index > length:
            raise InsertError("Insert Error: Out of Range.")

        if index == 0:
            self.add(elem)
        elif index == length:
            self.append(elem)
        else:
            node = LNode(elem)
            cur = self.head
            count = 0

            while count < index - 1:
                cur = cur.next
                count += 1

            node.next = cur.next
            cur.next = node

    #删除链表中某一位置的元素
    def remove(self, index):
        if self.isEmpty():
            raise IsEmpty("IsEmpty Error: The List is Empty.")

        length = self.length()
        if index < 0 or index >= length:
            raise RemoveError("Remove Error: Out of Range.")

        if index == 0:
            cur = self.head
            self.head = self.head.next
            cur.next = None
        else:
            cur = self.head
            count = 0

            while count < index - 1:
                cur = cur.next
                count += 1

            pre = cur
            cur = cur.next
            pre.next = cur.next
            cur.next = None