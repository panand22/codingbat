'''
Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
'''

def has22(nums):
    for i in range(1,len(nums)):
        if nums[i] == nums[i-1]and nums[i] ==2:
            return True
    return False