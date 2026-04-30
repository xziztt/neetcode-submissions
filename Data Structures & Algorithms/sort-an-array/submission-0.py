class Solution:

    def mergeSort(self,nums: List[int],left: int,right: int):
        if left >= right:
            return
        mid = left + (right - left)//2
        self.mergeSort(nums,left,mid)
        self.mergeSort(nums,mid+1,right)
        self.merge(nums,left,mid,right)

    
    def merge(self, nums: List[int], left: int, mid: int, right: int):
        
        leftList = nums[left:mid+1]
        rightList = nums[mid+1:right+1]
        i = 0
        j = 0
        k = left

        while i < len(leftList) and j < len(rightList):
            if leftList[i] < rightList[j]:
                nums[k] = leftList[i]
                i+=1
                k+=1
            else:
                nums[k] = rightList[j]
                j+=1
                k+=1
        
        while i < len(leftList):
            nums[k] = leftList[i]
            i+=1
            k+=1
        
        while j < len(rightList):
            nums[k] = rightList[j]
            j+=1
            k+=1
        






    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums,0,len(nums))
        return nums

        