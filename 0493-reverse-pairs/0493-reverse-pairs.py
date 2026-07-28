class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        # n=len(nums)
        # ans=0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         if nums[i] > 2 * nums[j]:
        #             ans += 1
        # return ans
        def merge_sort(l, r):
            if l >= r:
                return 0

            mid = (l + r) // 2

            count = merge_sort(l, mid)
            count += merge_sort(mid + 1, r)

            # Count reverse pairs
            j = mid + 1
            for i in range(l, mid + 1):
                while j <= r and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge step
            temp = []
            i, j = l, mid + 1

            while i <= mid and j <= r:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i += 1
                else:
                    temp.append(nums[j])
                    j += 1

            temp.extend(nums[i:mid + 1])
            temp.extend(nums[j:r + 1])

            nums[l:r + 1] = temp

            return count

        return merge_sort(0, len(nums) - 1)