#[3] -> [4]
#data   next
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
# 3을 가진 Node 를 만드려면 아래와 같이 하면 됨
node=Node(3)
# 노드들을 만들어서 연결해 보면
first_node=Node(5)
second_node = Node(12) # [12] 를 들고 있는 노드를 만듬
first_node.next=second_node #새로 만든 노드를 기존 노드로 연결

#위처럼 번거롭게 일일이 연결해주기 힘드므로
#링크드리스트를 이용
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)  # head 에 시작하는 Node 를 연결합니다.

# 맨 뒤의 노드까지 가기 위해서는 어떻게 해야 할까요?
# 현재 링크드 리스트는 다음과 같다고 합니다.
# head
# [3] → [5] → [6] → [8]

# 바로, head 를 따라서 계속 이동해야 합니다!
# head 를 변경시킬 수는 없으니, cur 이라는 변수를 이용해볼게요

# cur = this.head 에 넣으면 아래와 같이 되고,

# cur
# [3] → [5] → [6] → [8]

# cur = cur.next 을 하면 다음과 같이 한 칸 이동합니다.

#           cur
# [3] → [5] → [6] → [8]

# cur = cur.next 또 하면?

#                      cur
# [3] → [5] → [6] → [8]

    def append(self, value):     # LinkedList 가장 끝에 있는 노드에 새로운 노드를 연결합니다.
        cur = self.head         
        while cur.next is not None: # cur의 다음이 끝에 갈 때까지 이동합니다. 
            cur = cur.next          
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data,end=' ')
            cur=cur.next
        print()

linked_list = LinkedList(5)
print(linked_list.head.data) # 5가 출력됩니다!

linked_list.append(12)
# 이렇게 되면 5 -> 12 형태로 노드를 연결한 겁니다!
linked_list.append(8)
# 이렇게 되면 5 -> 12 -> 8 형태로 노드를 연결한 겁니다!
linked_list.print_all()