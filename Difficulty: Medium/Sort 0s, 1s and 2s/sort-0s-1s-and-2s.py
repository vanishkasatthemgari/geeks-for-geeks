#{ 
 # Driver Code Starts

# } Driver Code Ends

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        n=len(arr)
        l=0
        h=n-1
        mid=0
        while mid<=h:
            if arr[mid]==0:
                arr[l],arr[mid]=arr[mid],arr[l]
                l+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            else :
                arr[mid],arr[h]=arr[h],arr[mid]
                h-=1
        return arr
        


#{ 
 # Driver Code Starts.
def main():
    t = int(input().strip())  # Read the number of test cases
    ob = Solution()

    while t > 0:
        t -= 1
        arr = list(map(int,
                       input().strip().split())
                   )  # Read the array as space-separated integers
        ob.sort012(arr)  # Sort the array

        print(' '.join(map(str, arr)))  # Print the sorted array
        print("~")
        
if __name__ == "__main__":
    main()

# } Driver Code Ends