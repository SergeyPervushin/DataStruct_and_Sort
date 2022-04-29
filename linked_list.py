"""In this module we will create realization of three classes - Node, Singly linked list
and Doubly linked list. Class Node is the main class for create singly and doubly linked list classes"""
from sys import getsizeof


# class Node:
#     def __init__(self, data):
#         self.data = data  # current value af data
#         self.next = None  # reference to next element
#         self.previous = None  # reference to previous element
#
#     def has_value(self, value):
#         if self.data == value:
#             return True
#         else:
#             return False

class forward_linked_list_Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class doubly_linked_list_Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class Forward_List:
    def __init__(self, head):
        self.head = head

    def add_to_head(self):
        pass

    def add_to_end(self):
        pass

    def add_to_position(self):
        pass

    def remove_head(self):
        pass

    def remove_tail(self):
        pass

    def remove_val(self):
        pass

    def print(self):
        pass


class Doubly_List:
    def __init__(self, head):
        self.head = head


# class SinglyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def list_length(self):
#         """returns the number of list items"""
#         counter = 0  # initialization of counter that we will return after count of items
#         current_node = self.head  # first item initialization
#         while current_node is not None:  # run cycle while current node is not None
#             counter += 1
#             current_node = current_node.next  # make reference to next item of list
#         return counter  # return counter lol))))
#
#     def output_list(self):
#         """ printing all elements of list, its types and size in bytes?? """
#         current_node = self.head
#         while current_node is not None:
#             print(f'--{current_node.data}-- type: {type(current_node.data)} size of variable:(bytes) '
#                   f'{getsizeof(current_node.data)}')
#             current_node = current_node.next
#
#     def unordered_search(self, value):
#         """searching of all repeating items in list. Returns dict where kei is index, value is address of item"""
#         current_node = self.head
#         node_id = 1
#         result_of_search = {}
#         while current_node is not None:
#             if current_node.data == value:
#                 result_of_search[node_id] = hex(id(current_node))
#             current_node = current_node.next
#             node_id += 1
#         if len(result_of_search) == 0:
#             return f'There is no item in list. Lists address is {hex(id(self))}'
#         else:
#             return result_of_search
#
#     def remove_list_item_by_id(self, item_id):
#         """removing node in list by its index(if you know it)))"""
#         current_id = 1
#         current_node = self.head
#         previous_node = None
#         while current_node is not None:  # default cycle in this case
#             if current_id == item_id:  # you find needed id
#                 if previous_node is not None:  # if your node is not begin of list
#                     previous_node.next = current_node.next  # change ref
#                 else:
#                     self.head = current_node.next  # if node is begin, ref is node now))
#                     return
#             """ for iterate"""
#             previous_node = current_node
#             current_node = current_node.next
#             current_id += 1
#         return
#
#     def reverse(self):  # change only values(need changing objects)
#         if self.head is None:
#             return
#         stack = []
#         current_node = self.head
#         while current_node is not None:
#             stack.append(current_node.data)
#             current_node = current_node.next
#         current_node = self.head
#         while stack:
#             current_node.data = stack.pop()
#             current_node = current_node.next
#         return
#
#     """ adding item to list. default to end of list, if position is -1 - to end BULLSHIT!!!"""
#
#     def add(self, item, position=-1):
#         if not isinstance(item, Node):
#             item = Node(item)
#
#         if self.head is None:
#             self.head = item
#             self.tail = item
#             return
#         if position == 0:
#             temp = self.head
#             self.head = item
#             item.next = temp
#         else:
#             self.tail.next = item
#             self.tail = item
#
#     def insert(self, item, index=0):
#         if not isinstance(item, Node):
#             item = Node(item)
#         if self.head is None:
#             self.head = item
#             self.tail = item
#         counter = 0
#
#         pass
#
#
# """-----------------------------------------------------------------------------------"""
#
#
# class DoublyLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#
#     def add_list_item(self, item):
#         """add item to the end of the list"""
#         if not isinstance(item, Node):
#             item = Node(item)
#         if self.head is None:
#             self.head = item
#             item.next = None
#             item.previous = None
#             self.tail = item
#         else:
#             self.tail.next = item
#             item.previous = self.tail
#             self.tail = item
#
#     def output_list(self):
#         """ printing all elements of list, its types and size in bytes?? """
#         current_node = self.head
#         while current_node is not None:
#             print(f'--{current_node.data}-- {hex(id(current_node))}-- type: {type(current_node.data)} '
#                   f'size of variable:(bytes) '
#                   f'{getsizeof(current_node.data)}')
#             current_node = current_node.next
#
#     def list_length(self):
#         current_node = self.head
#         counter = 0
#         while current_node is not None:
#             counter += 1
#             current_node = current_node.next
#         return counter
#
#     def unordered_search(self, value):
#         current_node = self.head
#         node_id = 1
#         result_of_search = {}
#         while current_node is not None:
#             if current_node.has_value(value):
#                 result_of_search[node_id] = hex(id(current_node.data))
#             current_node = current_node.next
#             node_id += 1
#         return result_of_search
#
#     def remove_list_item_by_id(self, item_id):
#         node_id = 1
#         current_node = self.head
#
#         while current_node is not None:
#             prev_node = current_node.previous
#             next_node = current_node.next
#             if node_id == item_id:
#                 if prev_node is not None:
#                     prev_node.next = next_node
#                     if next_node is not None:
#                         next_node.previous = prev_node
#             else:
#                 self.head = next_node
#                 if next_node is not None:
#                     next_node.previous = None
#                 return
#
#             current_node = current_node.next
#             node_id += 1
#         return
#
#     def reverse(self):
#         current_head = self.head
#         current_tail = self.tail
#         while current_head:
#             current_head.data, current_tail.data = current_tail.data, current_head.data
#             if current_head.next == current_tail.next:
#                 return
#             if current_head.next == current_tail:
#                 return
#             current_head = current_head.next
#             current_tail = current_tail.previous
