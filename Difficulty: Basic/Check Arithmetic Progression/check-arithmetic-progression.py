class Solution:
    def checkIsAP(self, arr):
        #Your code goes here
        arr.sort()
        d=arr[1]-arr[0]
        for i in range(len(arr)-2,-1,-1):
            if abs(arr[i]-arr[i+1])!=d:
                return False
        return True
      



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.checkIsAP(arr)
        if ans:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends