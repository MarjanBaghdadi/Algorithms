class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        nums.sort()
        if len(nums) == 1:
            return False
        for i in range(len(nums)):
            if i == len(nums) - 1:
                break
            if nums[i] == nums[i + 1]:
                return True
            else:
                continue
        return False
    """
        
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
        

        
