#User function Template for python3

class Solution:
    def oppositeFaceOfDice(self, n):
    	#code here 
    	return 7-n


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.oppositeFaceOfDice(N)
        print(ans)

# } Driver Code Ends