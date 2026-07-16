class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
       arr=[]
       for i in range (0,m):
        arr.append(nums1[i])
       for i in range(0,n):
        arr.append(nums2[i])
       arr.sort()
       for i in range(0,len(arr)):
        nums1[i]=arr[i]
        
       return(nums1)
        