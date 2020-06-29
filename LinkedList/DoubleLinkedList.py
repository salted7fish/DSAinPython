from DSAinPython.LinkedList.MyError import *

#结点类
class DLNode:
    def __init__(self, elem=None, prev=None, next=None):
        self.elem = elem
        self.prev = prev
        self.next = next

#双链表类
class DoubleLinkedList:
    def __init__(self):
        self.head = self.rear = None

    def isEmpty(self):
        return self.head == None

    def length(self):
        count = 0
        cur = self.head

        while cur != None:
            cur = cur.next
            count += 1

        return count

    #打印输出链表中所有元素
    def show(self):
        cur = self.head

        while cur != None:
            print(cur.elem)
            cur = cur.next

    #在链表头部插入元素
    def add(self, elem):
        node = DLNode(elem)
        node.next = self.head
        self.head = node

    #在链表尾部插入元素
    def append(self, elem):
        node = DLNode(elem)

        if self.isEmpty():
            self.head = self.rear = node
        else:
            cur = self.rear
            cur.next = node
            node.prev = cur
            self.rear = node

    #在链表任意位置插入元素
    def insert(self, elem, index):
        length = self.length()
        if index > length:
            raise InsertError("Insert Error: Out of Range.")

        if index == 0:
            self.add(elem)
        elif index == length:
            self.append(elem)
        else:
            cur = self.head
            node = DLNode(elem)
            count = 0

            while count < index - 1:
                cur = cur.next
                count += 1

            node.next = cur.next
            node.prev = cur
            cur.next.prev = node
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
            self.head = cur.next
            self.head.prev = None
            cur.next = None
        elif index == length - 1:
            cur = self.rear
            self.rear = cur.prev
            self.rear.next = None
            cur.prev = None
        else:
            cur = self.head
            count = 0

            while count < index:
                cur = cur.next
                count += 1

            tmpPrev = cur.prev
            tmpNext = cur.next
            tmpPrev.next = cur.next
            tmpNext.prev = cur.prev
            cur.next = cur.prev = None
