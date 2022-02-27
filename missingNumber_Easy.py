class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        solutionMap = {}
        for i in nums:
            solutionMap[i] = i
        for i in range(len(nums)+2):
            if i not in solutionMap:
                return i
        
                      
        """
        # XOR solution: if we XOR all the numbers with all the indices(+1 extra for the missing number) 
        # the only missing number will be the one left over at the end 
        
        solution = 0
        
        for n in nums:
            solution = solution ^ n
            
        for i in range(len(nums)+1):
            solution = solution ^ i
              
        return solution
        """
