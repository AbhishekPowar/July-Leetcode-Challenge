class Solution:
    def zigzagLevelOrder(self, root):
        def height(root):
            if root:
                return max(height(root.left), height(root.right))+1
            else:
                return 0

        def addToAns(lvl, node):
            if node and lvl < self.height:
                self.ans[lvl].append(node.val)
                addToAns(lvl+1, node.left)
                addToAns(lvl+1, node.right)

        self.height = height(root)
        self.ans = [list() for i in range(self.height)]

        addToAns(0, root)
        for idx, val in enumerate(self.ans):
            if idx % 2 == 1:
                self.ans[idx].reverse()
        return self.ans
