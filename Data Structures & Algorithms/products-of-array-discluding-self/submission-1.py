class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        
        # Start with 1 for every position
        output = [1] * n
        
        # Step 1: Store product of everything on the LEFT
        left_product = 1
        
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]
        
        # Step 2: Multiply by product of everything on the RIGHT
        right_product = 1
        
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]
        
        return output