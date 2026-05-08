class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,2,2,3,3,3]
        # {1:1, 2:2, 3:3}
        count = {}

        for num in nums:

            # if the number exist in count
            if num in count:
                # set value +=1 
                count[num] +=1

            else:
                count[num] = 1
            

        # sort count
        sorted_items = sorted(count, key=count.get, reverse=True)
        return sorted_items[:k]
        # return key that has most count.values()