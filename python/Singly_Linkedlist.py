#create Node
class Node:
  def __init__(self,data=0,next=None):
    self.data=data
    self.next=next

#combine list to calulate
class sumlist:
  def tosums(self,list_1: Node,list_2: Node) -> Node:
    cur=res=Node()
    carry=0
    while list_1 or list_2 or carry:
        if list_1:
            carry += list_1.data
            list_1=list_1.next
        if list_2:
            carry += list_2.data
            list_2=list_2.next
        carry,value = carry //10,carry%10
        cur.next = Node(value)
        cur = cur.next
    return res.next


sets= sumlist()
#insert
list_1 = Node(77)
list_2 = Node(85)
list_3 = Node(71)
#swapeed
list_1.next=list_2
list_2.next=list_3
#insert
list2_1 = Node(66)
list2_2 = Node(67)
list2_3 = Node(68)
#swaped
list2_1.next=list2_2
list2_2.next=list2_3
result = sets.tosums(list_1,list_2)
while result:
  print(result.data)
  result=result.next
  


