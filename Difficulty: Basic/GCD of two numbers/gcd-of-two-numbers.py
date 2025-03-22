
class Solution:
    def gcd(self, a : int, b : int) -> int:
        # code here
        """if a==b:
            return a
        if a==0:
            return b
        if b==0:
            return a
        if a>b:
            return self.gcd(a-b,b)
        return self.gcd(a,b-a)
        mini=min(a,b)
        while mini:
            if a%mini==0 and b%mini==0:
                break
            mini-=1
        return mini"""
        if b==0:
            return a
        return self.gcd(b,a%b)



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        a = int(input())

        b = int(input())

        obj = Solution()
        res = obj.gcd(a, b)

        print(res)

        print("~")

# } Driver Code Ends