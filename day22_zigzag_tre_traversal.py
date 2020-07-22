class Solution:
    def zigzagLevelOrder(self, root):
        def height(root):
            if root:
                return max(height(root.left),height(root.right))+1
            else:
                return 0

        def addToQueue(lvl,node):
            if node and lvl<self.height:
                self.ans[lvl].append(node.val)
                addToQueue(lvl+1,node.left)
                addToQueue(lvl+1,node.right)
                
            
        self.height = height(root)
        self.ans = [list() for i in range(self.height)]
        
        from collections import deque
        

        addToQueue(0,root)
        for idx,val in enumerate(self.ans):
            if idx%2==1:
                self.ans[idx].reverse()
        return self.ans