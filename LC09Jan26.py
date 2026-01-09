# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans = [0, root]
        def solve(r, level):
            nonlocal ans
            
            dl = dr = level
            if r.left:
                dl = solve(r.left, level + 1)
            if r.right:
                dr = solve(r.right, level + 1)

            mxd = max(dl, dr)
            if mxd > ans[0] or dl == dr and dl == ans[0]:
                ans = [mxd, r]
            return mxd

        solve(root, 0)
        return ans[1]
        
