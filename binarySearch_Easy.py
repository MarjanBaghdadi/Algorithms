class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #with recursion:
        
        self.nums = nums
        self.target = target
        l=0
        h=len(nums)-1
        return self.searchRecursionFunction(l,h) 
    
    def searchRecursionFunction(self, low , high):
        if low > high:
            return -1
        mid = (high + low) // 2
        print(mid)

        if self.target == self.nums[mid]:
            return mid
        elif self.target < self.nums[mid]:
            return self.searchRecursionFunction(low, mid-1)
        else:
            return self.searchRecursionFunction(mid+1, high)
