class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for e in nums:
        
            if e not in seen:
                seen.add(e);
        
            else:
                return True;

        return False;