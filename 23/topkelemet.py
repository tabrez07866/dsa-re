from collections import Counter

def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        counter = Counter(nums)
        bucket = [0] * (n + 1)  # keep this line unchanged

        for num, freq in counter.items():
            if bucket[freq] == 0:
                bucket[freq] = [num]  # first time, create a list
            else:
                bucket[freq].append(num)  # append to existing list

        ret = []
        for i in range(n, -1, -1):
            if bucket[i] != 0:
                for item in bucket[i]:
                    ret.append(item)
                    if len(ret) == k:
                        return ret
        return ret

nums=[2,2,1,1,3,5,5,5]
ret=topKFrequent(nums,2)
print(ret)

