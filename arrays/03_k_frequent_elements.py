from typing import List
class Solution:
    # the time complexity is O(m log m) where m is the number of unique elements
    # the space complexity is O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        sorted_keys = sorted(counts, key=counts.get, reverse=True)
        return sorted_keys[:k]


nums, k = [1,2,2,3,3,3], 2
output = Solution()
print("topKFrequent", output.topKFrequent(nums, k))
