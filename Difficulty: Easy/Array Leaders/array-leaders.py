class Solution:
    def leaders(self, arr):
        # code here
        a=[]
        maxi=0
        for i in range(len(arr)-1,-1,-1):
            if arr[i]>=maxi:
                a.append(arr[i])
                maxi=arr[i]
        return a[::-1]


#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends