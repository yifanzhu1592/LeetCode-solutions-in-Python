# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(in_left, in_right):
            
            nonlocal postorder_index
            
            # if there is no elements to construct subtrees
            if in_left > in_right:
                return None
            
            # pick up the last element as a root
            val = postorder[postorder_index]
            root = TreeNode(val)
            
            postorder_index -= 1

            
            # build right subtree
            root.right = helper(idx_map[val] + 1, in_right)
            # build left subtree
            root.left = helper(in_left, idx_map[val] - 1)
            return root
        
        postorder_index = len(postorder) - 1
        
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper(0, len(inorder) - 1)
