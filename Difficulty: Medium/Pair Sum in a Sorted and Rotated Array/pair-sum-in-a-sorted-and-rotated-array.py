#User function Template for python3

class Solution:
    ##Complete this function
    def pairInSortedRotated(self,arr, target):
        #Your code here
        s=set()
        for i in arr:
            res=target-i
            if res in s:
                return True
            s.add(i)
        return False
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        A = [int(x) for x in input().strip().split()]
        target = int(input())
        ob = Solution()
        print("true" if ob.pairInSortedRotated(A, target) else "false")
        print("~")

# } Driver Code Ends