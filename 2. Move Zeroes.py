class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag=False
        j=1
        for i in range(len(nums)-1):
            for j in range(j,len(nums)):
                if nums[i]==0:
                    if nums[j]!=0:
                        flag=nums[i]
                        nums[i]=nums[j]
                        nums[j]=flag
                        j+=1
                        break
                else:
                    j+=1
                    break
