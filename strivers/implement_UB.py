#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        
        floor = -1
        sheila = -1
        
        for i,num in enumerate(arr):
            if num <= x and num >= (lambda mf: mf if mf != -1 else num-1)(floor):
                floor = num
        
        for i,num in enumerate(arr):
            if num >= x and num <= (lambda mf: mf if mf != -1 else num+1)(sheila):
                sheila = num
                
        return [floor,sheila]
        