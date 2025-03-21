#User function Template for python3

class Solution:
	def reverseDigits(self, n):
		# Code here
		n=list(str(n))
		l=0
		h=len(n)-1
		while l<h:
		    n[l],n[h]=n[h],n[l]
		    l+=1
		    h-=1
	    return int("".join(n))
		 


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        ob = Solution()
        ans = ob.reverseDigits(n)
        print(ans)

        print("~")

# } Driver Code Ends