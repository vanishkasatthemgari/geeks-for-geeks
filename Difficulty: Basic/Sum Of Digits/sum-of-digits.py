#User function Template for python3

class Solution:
    def sumOfDigits (self, n):
        # code here
        s=0
        while n>0:
            s+=int(n%10)
            n/=10
        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.sumOfDigits(N))
        print("~")

# } Driver Code Ends