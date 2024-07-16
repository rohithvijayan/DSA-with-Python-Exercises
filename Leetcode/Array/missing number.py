'''
Missing Number
Given an array nums containing n distinct numbers in the range [0, n], 
return the only number in the range that is missing from the array.
'''
class Solution(object):
    def missingNumber(self, nums):
        length=len(nums)
        for i in range(0,length+1):
            if i not in nums:
                return i
sol=Solution()
test1=sol.missingNumber(nums=[3,0,1])
print(test1)
test2=sol.missingNumber(nums=[0,1,2,3])
print(test2)