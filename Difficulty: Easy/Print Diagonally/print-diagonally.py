#User function Template for python3

def downwardDiagonal(N, A): 
    # code here \
    res=[]
    for r in range(N):
        i=0
        j=r
        while i<N and j>=0:
            res.append(A[i][j])
            i+=1
            j-=1
    for k in range(1,N):
        i=k
        j=N-1
        while i<N and j>=0:
            res.append(A[i][j])
            i+=1
            j-=1
    return res
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix =[]
        for i in range(n):
            row = list(map(int, input().strip().split()))
            matrix.append(row)
        ans = downwardDiagonal(n,matrix)
        for i in ans:
            print(i,end=" ")
        print()

        print("~")
# } Driver Code Ends