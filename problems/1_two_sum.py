class Solution(object):
    def twoSum(self, nums, target):
        indices = []
        for i in range(len(nums)):
            num = nums[i]
            if i < (len(nums) - 1):
                j = i + 1
                while j < len(nums): 
                    second_num = nums[j]
                    sum = num + second_num
                    if sum == target:
                        indices.append(i)
                        indices.append(j)
                        return indices
                    j += 1