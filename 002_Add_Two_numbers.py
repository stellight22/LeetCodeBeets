# Add two numbers
# 10/14/2021

#Approach
'''
'''
#Time complexity
''' 
'''
#space complexity
'''
'''
#Mistakes Made
'''
'''
#code

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from _typeshed import SupportsKeysAndGetItem


class Solution:
    def addTwoNumbers(self, l1, l2):
        list1 = [] #empty lists for reverse list storage
        list2 = []
        for num in l1: # for loop to store reversed lists
            for x in range(len(l1)-1,0,-1):
                list1.append(l1[x])
        for n in l2:
            for u in range(len(l2)-1, 0, -1):
                list2.append(l2[x])
        sumlist = []   # to store sum of two lists
        sum = list1[x] + list2[x]
        length1 = len(list1)
        length2 = len(list2)
        extra = 0
        if length1 > length2:   # for different lengths of lists
            extra = length1 - length2
            for x in range(0,extra):
                sumlist.append(list1[x])
            for x in range(0,len(length2)):
                sumlist.append
        if length2 > length1:
            extra = length2 - length1
            for x in range(0,extra):
                sumlist.append(list2[x])
        if length1 == length2:
            for x in range(0, len(list1)):
                sumlist.append(sum)
        print(sumlist)

    
    





