class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def TEST(nums):
            if len(nums) < 2  :  
                return  nums
            cpt =  nums[0]  + nums[1]
            right = 0  
            for i in  range(len(nums) -1) :   
                var  = nums[i+1] + nums[i]    
                if var  < cpt :    
                    right =  i   
                    cpt =  var 
            nums.pop(right)
            nums.pop(right)     
            nums.insert(right, cpt)  
            return nums   
        opr = 0   
        while True :   
            srtd = True   
            for i in range (len(nums) -1) :   
                if nums[i] > nums[i+1] : 
                    srtd =  False   
                    break   
            if srtd or len(nums) <= 1 : 
                break   
            nums = TEST (nums)   
            opr +=  1  
        return opr   
        
