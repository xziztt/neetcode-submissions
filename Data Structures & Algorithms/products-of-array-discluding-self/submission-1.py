class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        arr1 = []
        currProduct = 1
        for i in nums:
            currProduct *= i
            arr1.append(currProduct)

        arr2 = []
        currProduct = 1
        for i in range(len(nums) - 1,-1,-1):
            currProduct *= nums[i]
            arr2.insert(0,currProduct)
            
        print(arr1)
        print(arr2)

        finalArr = [arr2[1]]
        for i in range(1,len(nums) - 1):
            finalArr.append(arr1[i - 1] * arr2[i+1])
        
        finalArr.append(arr1[-2])

        return finalArr