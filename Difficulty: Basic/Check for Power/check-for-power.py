#User function Template for python3
import math
class Solution:
    def isPowerOfAnother (ob,x,y):
        # code here 
        if x==1:
            return False
        res=math.log(y)/math.log(x)
        return res==math.floor(res)
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        X, Y = map(int, input().strip().split(" "))

        ob = Solution()
        ans = ob.isPowerOfAnother(X, Y)

        print("True" if ans else "False")
        print("~")

# } Driver Code Ends