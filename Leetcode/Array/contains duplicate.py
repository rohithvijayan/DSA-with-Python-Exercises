'''
Topics
Companies

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true

Example 2:

Input: nums = [1,2,3,4]
Output: false

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
class Solution(object):
    def containsDuplicate(self, nums):
        count=1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    count+=1
                    if count>1:
                        return True

sol=Solution()
test1=sol.containsDuplicate(nums=[1,2,3,1])
print(test1)
test2=sol.containsDuplicate(nums=[1,2,3,4])
print(test2)
test3=sol.containsDuplicate(nums=[1,1,1,3,3,4,3,2,4,2])
print(test3)