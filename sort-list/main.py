class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        node = Node(data,None)
        
        if self.head ==None:
            self.head =node

        else:
            curr = self.head
            while curr.next:
                curr = curr.next

            curr.next = node

    def display(self):
        curr = self.head
        linked_list_string = ""

        while curr:
            linked_list_string += str(curr.data) + '----->'
            curr=curr.next
        
        linked_list_string += "END"
        print(linked_list_string)

    def asc_sort(self,head):
        if not head or not head.next:
            return head
        
        left = head
        mid = self.getMid(head)
        right = mid.next
        mid.next = None

        left_sorted = self.asc_sort(left)
        right_sorted = self.asc_sort(right)

        return self.merge(left_sorted,right_sorted)

    def getMid(self,head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self,left,right):
        dummy = Node()
        tail = dummy

        while left and right:
            if left.data < right.data:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        tail.next = left or right

        return dummy.next
    def sort(self):
        self.head = self.asc_sort(self.head)



ll = LinkedList()
ll.append(5)
ll.append(3)
ll.append(4)
ll.append(1)

ll.display()
ll.sort()
ll.display()
