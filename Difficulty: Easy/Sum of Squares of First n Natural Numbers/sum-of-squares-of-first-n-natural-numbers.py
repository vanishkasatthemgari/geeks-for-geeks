#User function Template for python3
class Solution:
    # Function to calculate the sum of squares of first 'number' natural numbers
    def sumOfSquares(self, number):
        # code here
        return (number * (number+1) * (2*number+1))//6

#{ 
 # Driver Code Starts
#Position this line where user code will be pasted.
# Driver code
t = int(input())
ob = Solution()

for _ in range(t):
    number = int(input())
    ans = ob.sumOfSquares(number)
    print(ans)
    print("~")

# } Driver Code Ends