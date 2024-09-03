# Heaps-1

## Problem 1 Kth largest in Array (https://leetcode.com/problems/kth-largest-element-in-an-array/)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
# Min heap
        if nums == None or len(nums) == 0:
            return -1
        pq = heapq
        li= []
        for i in range(len(nums)):
            pq.heappush(li,nums[i])
            if len(li)> k:
                pq.heappop(li)
        return pq.heappop(li)

# Min heap and maintaining k elements - TC = O(nlogk); SC = O(k) --> preffered solution for largest


## Problem 2 Merge k Sorted Lists(https://leetcode.com/problems/merge-k-sorted-lists/)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists):
        if lists == None or len(lists) == 0:
            return None
      
        merged = ListNode(-sys.maxsize-1)
        for l in lists:
            merged = self.merge(merged,l)
        return merged.next

    def merge(self,l1,l2 ):
        dummy = ListNode(-1)
        curr = dummy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2= l2.next
            curr = curr.next
        if l1!= None:
            curr.next = l1
        if l2!= None:
            curr.next = l2
        return dummy.next
