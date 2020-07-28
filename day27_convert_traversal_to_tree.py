# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# better solution will be added


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def Tree(inOrder, postOrder):
            if len(inOrder) > 1:
                root = TreeNode(postOrder[-1])
                mid = inOrder.index(postOrder[-1])
                root.left = Tree(inOrder[:mid], postOrder[:mid])
                if mid+1 < len(inOrder):
                    root.right = Tree(inOrder[mid+1:], postOrder[mid:-1])
                else:
                    root.right = None
                return root
            else:
                if len(inOrder):
                    return TreeNode(inOrder[0])
                else:
                    return None
        return Tree(inorder, postorder)
