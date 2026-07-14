class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l=0
        r=len(people)-1
        people=sorted(people)
        cnt=0
        while l<=r:
            s=people[l]+people[r]
    
            if s<=limit:
                l+=1
            r-=1
            cnt+=1

        return cnt




        