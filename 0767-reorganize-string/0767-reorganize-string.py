import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        l=collections.Counter(s)
        maxheap=[[-cnt,c] for c,cnt in l.items()]
        heapq.heapify(maxheap)
        prev=None
        ans=""
        while maxheap or prev:
            if prev and not maxheap:
                return ""
            cnt,c=heapq.heappop(maxheap)
            cnt+=1
            ans+=c
            if prev:
                heapq.heappush(maxheap,prev)
                prev=None
            if cnt!=0:
                prev=[cnt,c]
        return ans