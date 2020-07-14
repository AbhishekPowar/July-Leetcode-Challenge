def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def inorder(root,arr):
            if root:
                arr.append(root.val)
                inorder(root.left,arr)
                inorder(root.right,arr)
                return arr
            else:
                arr.append(None)
                
        parr = inorder(p,[])
        qarr = inorder(q,[])
        return parr == qarr
