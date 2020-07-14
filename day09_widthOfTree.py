class Node:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def widthOfBinaryTree(root):
    def height(root):
        if root:
            return 1+max(
                height(root.left),
                height(root.right),
            )
        else:
            return 0

    def width(root, meta=[0, 0, 0]):
        if root:
            msb, lsb, level = meta
            value = (msb*2)+lsb
            if widthArray[level][0] == -1:
                widthArray[level][0] = value
            else:
                widthArray[level][1] = value
            level += 1
            width(root.left, [value, 0, level])
            width(root.right, [value, 1, level])

    h = height(root)
    widthArray = [[-1, -1] for i in range(h+1)]
    width(root)
    ans = max(*widthArray, key=lambda x: x[1]-x[0])
    return ans[1]-ans[0]+1


if __name__ == "__main__":
    n9 = Node(9)
    n8 = Node(8)
    n8 = Node(8)
    n7 = Node(7)
    n6 = Node(6)
    n5 = Node(5)
    n4 = Node(4)
    n3 = Node(3)
    n2 = Node(2)
    n1 = Node(1)

    n1.left = n3
    # n1.right = n2
    # n3.left = n5
    # n2.right = n9
    # n5.left = n6
    # n9.right = n7

    # n1.left = n3
    # n3.left = n5
    # n1.right = n2
    # n2.right = n6
    print(widthOfBinaryTree(n1))
