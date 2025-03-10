#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n=len(arr)
        freq=[0]*(n+1)
        m=-1
        r=-1
        for i in range(n):
            freq[arr[i]]+=1
        for i in range(1,n+1):
            if freq[i]==0:
                m=i
            elif freq[i]>1:
                r=i
        return [r,m]
                
            




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends