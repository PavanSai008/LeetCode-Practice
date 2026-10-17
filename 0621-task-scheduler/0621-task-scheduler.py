class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        freq=collections.Counter(tasks)
        max_f=max(freq.values())
        max_c=sum(1 for f in freq.values() if f==max_f)
        return max(len(tasks),(max_f-1)*(n+1)+max_c)