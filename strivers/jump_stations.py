class Solution:
    def maxPower(self, stations, r: int, k: int) -> int:
        n = len(stations)

        diff = [0]*(n+1)
        for i, s in enumerate(stations):
            L = max(0, i-r)
            R = min(n-1, i+r)
            diff[L] += s
            diff[R+1] -= s

        base = [0]*n
        cur = 0
        for i in range(n):
            cur += diff[i]
            base[i] = cur

        def can(x: int) -> bool:
            need = k         
            d2 = [0]*(n+1)   
            added = 0
            for i in range(n):
                added += d2[i]
                v = base[i] + added
                if v < x:
                    add = x - v
                    if add > need: return False
                    need -= add
                    added += add
                    j = min(n-1, i+r)
                    end = j + r
                    if end+1 < n:
                        d2[end+1] -= add
            return True

        lo, hi = min(base), min(base)+k+10**18 
        ans = lo
        while lo <= hi:
            mid = (lo+hi)//2
            if can(mid):
                ans = mid
                lo = mid+1
            else:
                hi = mid-1
        return ans
