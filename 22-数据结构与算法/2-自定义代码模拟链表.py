
class SingleNode:
    def __init__(self,item):
        self.item = item
        self.next = None

class SingleLinkedList:
    def __init__(self,node= None):
        self.head = node

    def is_empty(self):
        #     if self.head == None:
        #         return True
        #     else:
        #         return False

       # self.head is None 就是一个布尔值
       #  return True if self.head is None else False
         return self.head is None

    def length(self):
        cur = self.head
        count = 0
        while cur is not None:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        cur = self.head
        while cur is not None:
            print(cur.item)
            cur = cur.next

    def add(self,item):
        new_node = SingleNode(item)
        new_node.next = self.head
        self.head = new_node

    def append(self,item):
        new_node = SingleNode(item)
        if self.is_empty():
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node

    def insert(self,pos,item):
        if pos <=0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:
            count=0
            cur = self.head
            while count < pos -1:
                cur = cur.next
                count +=1
            new_node = SingleNode(item)
            new_node.next = cur.next
            cur.next = new_node



if __name__ == '__main__':

    # print(f'元素域（数字域）:{SingleNode(20).item}')
    # print(f'指针域：{SingleNode(20).next}'
    # node1 = SingleNode(10)
    # print(f'元素域（数字域）:{node1.item}')
    # print(f'链接域（地址域）:{node1.next}')
    # print(f'node1对象：{node1}')
    # print(f'node1的类型：{type(node1)}')
    # print('-' *23)
    #
    # my_ll = SingleLinkedList(node1)
    # print(f'头节点为:{my_ll.head}')
    # print(f'头结点的元素域：{my_ll.head.item}')
    # print(f'头结点的地址域：{my_ll.head.next}')


    # node1 = SingleNode('altersu')
    # my_ll = SingleLinkedList(node1)
    # print(my_ll.head)
    # print(my_ll.head.item)
    # print(my_ll.is_empty())

    node1 = SingleNode('alter')
    print(node1.item)
    my_ll = SingleLinkedList(node1)
    my_ll.add('su')
    my_ll.add('python')
    print(my_ll.length())
    my_ll.append('is')
    my_ll.append('good')
    my_ll.insert(2,'language')
    my_ll.insert(10,'zhang')

    my_ll.travel()