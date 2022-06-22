class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counts = collections.Counter(nums)
        sort_counts = sorted(counts.items(), key=lambda x: x[0], reverse=True)
        
        for key, value in sort_counts:
            k -= value
            if k <= 0:
                return key