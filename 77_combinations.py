


def combine(n: int, k: int):
    ans = [] 
    def dfs(i, curr_sol):
        if len(curr_sol) == k:
            ans.append(curr_sol.copy())
            return
        
        for num in range(i + 1, n + 1):
            curr_sol.append(num)
            dfs(i + 1, curr_sol)
            curr_sol.pop()

    dfs(0, []) 

    return ans


res = combine(4, 2)
print(res)



       
