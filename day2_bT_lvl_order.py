 def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
       
        def display(self, lvl=0, arr=[]):
            # print(lvl)
            if self.left != None:
                display(self.left,lvl+1,arr)

            if self.right != None:
                display(self.right,lvl+1,arr)
            # print(f'data = {self.val}')
            arr[lvl].append(self.val)
            return arr


        def height(self):
            if self.left==None:
                l=0
            else:
                l = height(self.left)

            if self.right==None:
                r=0
            else:
                r = height(self.right)
            return max(l,r)+1
        if root:
            hi = height(root)
            arr = [[] for i in range(hi)]
            ans = display(root,0, arr)
            return ans[::-1]
        else:
            return []
