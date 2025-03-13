class Solution:
    def thirdLargest(self,arr):
        # code here
        arr.sort()
        return arr[-3]


#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().strip().split()))
        print(Solution().thirdLargest(arr))
        print("~")

# } Driver Code Ends