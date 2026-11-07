class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r=deque()
        d=deque()
        for i,x in enumerate(senate):
            if x=='R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
            rturn=r.popleft()
            dturn=d.popleft()
            if rturn<dturn:
                r.append(rturn+len(senate))
            else:
                d.append(dturn+len(senate))
        return "Radiant" if r else "Dire"