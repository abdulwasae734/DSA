class Solution:
    def longestSubarray(self, arr, k):
        maxlen = 0
        for j in range(len(arr)):
            cur_sum = 0
            
            for i in range(j,len(arr)):
                cur_sum += arr[i]
                if cur_sum == k:
                    cur_len = i - j + 1
                    if cur_len > maxlen:
                        maxlen = cur_len
        
        return maxlen