# Definition for singly-linked list.
class ListNode:
    def __init__(self, data):
        self.val = data
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """ 
        def insert_node(node1,node2):
            if node1.next == None:
                node1.next = node2
            else:
                p = node1
                while p.next:
                    #print("1111")
                    p = p.next
                p.next = node2
            return node1
        

        """
        X + X =
        X + XXXXX =
        """
        carry_bit = 0
        if l1.next == None:           
            if l1.val + l2.val < 10:
                node = ListNode(l1.val + l2.val)
                carry_bit = 0
            else:
                node = ListNode(l1.val + l2.val - 10)
                carry_bit = 1
            #print("XXX")
            l3_head = node
            if l2.next == None:
                if carry_bit == 1:                   
                    insert_node(l3_head,ListNode(carry_bit))
                return l3_head
            else:
                #insert_node(l3_head,node)
                while l2.next:
                    #print("XXX")
                    if l2.next.val + carry_bit < 10:
                        node = ListNode(l2.next.val + carry_bit)
                        carry_bit = 0
                    else:
                        node = ListNode(l2.next.val + carry_bit - 10)
                        carry_bit = 1          
                    insert_node(l3_head,node)
                    l2 = l2.next
                if carry_bit == 1:
                    insert_node(l3_head,ListNode(carry_bit))
                return l3_head

        #carry_bit = 0 
        i=0
        while l1.next:
            ### XX + XX           
            if l2.next:
                if l1.val + l2.val + carry_bit < 10:
                    node = ListNode(l1.val + l2.val + carry_bit)
                    carry_bit = 0
                else:
                    node = ListNode(l1.val + l2.val + carry_bit - 10)
                    carry_bit = 1
                if i == 0:
                    l3_head = node
                else:     
                    insert_node(l3_head,node)
            ### XXXXX + X =
            ### XXX + XX
            else:
                if l1.val + l2.val + carry_bit < 10:
                    node = ListNode(l1.val + l2.val + carry_bit)
                    carry_bit = 0
                else:
                    node = ListNode(l1.val + l2.val + carry_bit - 10)
                    carry_bit = 1
                if i == 0:
                    l3_head = node
                else:
                    insert_node(l3_head,node)
                while l1.next:
                    if l1.next.val + carry_bit < 10:
                        node = ListNode(l1.next.val + carry_bit)
                        carry_bit = 0
                    else:
                        node = ListNode(l1.next.val + carry_bit - 10)
                        carry_bit = 1
                    insert_node(l3_head,node)
                    l1 = l1.next
                if carry_bit == 1:
                    insert_node(l3_head,ListNode(carry_bit))
                return l3_head

            l1 = l1.next
            l2 = l2.next
            i = i + 1
        #print("XXX")
        #print(l1.val)
        #print(l2.val)
        #print(carry_bit)
        ##Last data
        if l1.val + l2.val + carry_bit < 10:
            #print("l1.val + l2.val + carry_bit")
            #print(l1.val + l2.val + carry_bit)
            node = ListNode(l1.val + l2.val + carry_bit)
            carry_bit = 0
        else:
            node = ListNode(l1.val + l2.val + carry_bit - 10)
            carry_bit = 1
        insert_node(l3_head,node)
        
              
        ###l2 length > l1 length 
        while l2.next:
           # print("mmmmm")
            if l2.next.val + carry_bit < 10:
                node = ListNode(l2.next.val + carry_bit)
                carry_bit = 0
            else:
                node = ListNode(l2.next.val + carry_bit - 10)
                carry_bit = 1          
            insert_node(l3_head,node)
            l2 = l2.next
        if carry_bit == 1:
            insert_node(l3_head,ListNode(carry_bit))
        return l3_head   

def insert_node(node1,node2):
    if node1.next == None:
        node1.next = node2
    else:
        p = node1
        while p.next:
            p = p.next
        p.next = node2
    return node1

if __name__ == "__main__":
    
  
    i = 0 
    for item in [3,1,1]:
        if i == 0:
            listnode1 = ListNode(item)
        else:
            insert_node(listnode1,ListNode(item))
        i = i + 1 
    
    i = 0
    for item in [1,1,4,5,6]:
        if i == 0:
            listnode2 = ListNode(item)
        else:
            insert_node(listnode2,ListNode(item))    
        i = i + 1
    
    Solution1 = Solution()
    node3 = Solution1.addTwoNumbers(listnode1,listnode2)

    while node3.next:
        print(node3.val)
        node3 = node3.next
    print(node3.val)

    
