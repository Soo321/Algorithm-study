from collections import Counter
import operator

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = Counter(nums)
        sorted_dict = dict(sorted(nums_dict.items(), key = operator.itemgetter(1), reverse = True))

        return list(sorted_dict.keys())[:k]
        