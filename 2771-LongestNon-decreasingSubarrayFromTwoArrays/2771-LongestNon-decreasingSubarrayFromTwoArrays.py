# Last updated: 26/02/2026, 20:52:11
1# class Solution:
2#     def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
3#         #(i,last) : max
4#         memo = defaultdict(int)
5#         def find_max(i,current_length,last):
6#             if i >= len(nums1):
7#                 return current_length
8#             if (i,last) in memo:
9#                 return memo[(i,last)]
10#             mn = min(nums1[i],nums2[i])
11#             mx = max(nums1[i],nums2[i])
12
13#             if mn >= last: 
14#                 memo[(i,mn)] = find_max(i+1,current_length+1,mn)
15#             else:
16#                 if max(nums1[i],nums2[i]) >= last:
17#                     memo[(i,mx)] = find_max(i+1,current_length+1,mx)
18#                 memo[(i,mn)] = find_max(i+1,1,mn)
19
20#             return max(memo[(i,mx)] ,memo[(i,mn)] )
21        
22#         return find_max(1,1,min(nums1[0],nums2[0]))
23            
24
25class Solution:
26    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
27        n = len(nums1)
28        dp1 = [1] * n  # ends with nums1[i]
29        dp2 = [1] * n  # ends with nums2[i]
30
31        for i in range(1, n):
32            # Extending a sequence ending at i-1 into index i
33            if nums1[i] >= nums1[i-1]:
34                dp1[i] = max(dp1[i], dp1[i-1] + 1)
35            if nums1[i] >= nums2[i-1]:
36                dp1[i] = max(dp1[i], dp2[i-1] + 1)
37            if nums2[i] >= nums1[i-1]:
38                dp2[i] = max(dp2[i], dp1[i-1] + 1)
39            if nums2[i] >= nums2[i-1]:
40                dp2[i] = max(dp2[i], dp2[i-1] + 1)
41
42        return max(max(dp1), max(dp2))