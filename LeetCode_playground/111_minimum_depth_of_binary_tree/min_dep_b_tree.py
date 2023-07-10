"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:

The number of nodes in the tree is in the range [0, 10^5].
-1000 <= Node.val <= 1000
"""
from typing import Optional

TEST_CASES = [
    [3, 9, 20, None, None, 15, 7],  # test case 1
    [2, None, 3, None, 4, None, 5, None, 6]  # test case 2
]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        left_depth = self.minDepth(root.left)  # This is function with next node
        right_depth = self.minDepth(root.right)

        if left_depth is None and right_depth is None:
            return 1

        if root.left is None:
            return 1 + right_depth

        if root.right is None:
            return 1 + left_depth

        return min(left_depth, right_depth) + 1


if __name__ == '__main__':
    solution = Solution()
    for CASE in TEST_CASES:
        root = TreeNode(CASE[0])
        current = root
        queue = [current
                 ]
        for value in CASE[1:]:
            if value is not None:
                node = TreeNode(value)
                current.left = node
                queue.append(node)
            else:
                current.left = None

            if len(queue) > 1:
                current = queue.pop(0)

        print(solution.minDepth(root))
