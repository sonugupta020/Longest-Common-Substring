class Solution:
    def longestCommonSubstr(self, S1, S2, a, b):
        dp = [[-1 for _ in range(b)] for _ in range(a)]
        def rec(i,j):   
            if i<0 or j<0:     
                return 0

            if dp[i][j] == -1:
                if S1[i] == S2[j]:
                    dp[i][j] = 1+rec(i-1,j-1)
                else:
                    dp[i][j] = 0
            return dp[i][j]

        ans = 0
        for i in range(a):
            for j in range(b):
                ans = max(ans, rec(i,j))
        return ans

if __name__=='__main__':
     t=int(input())
     for _ in range(t):

        a,b = input().strip().split(" ")
        a,b = int(a), int(b)
        S1 = input().strip()
        S2 = input().strip()
           
        sonu = Solution()
        print(sonu.longestCommonSubstr(S1, S2, a, b))
