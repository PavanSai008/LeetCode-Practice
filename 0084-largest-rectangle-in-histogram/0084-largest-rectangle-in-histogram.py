class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack=[]
        max_a=0
        for i in range(len(heights)):
            satrt=i
            while stack and heights[i]<stack[-1][0]:
                h,j=stack.pop()
                w=i-j
                max_a=max(max_a,h*w)
                satrt=j
            stack.append((heights[i],satrt))
        while stack:
            h,j=stack.pop()
            w=len(heights)-j
            max_a=max(max_a,h*w)
        return max_a