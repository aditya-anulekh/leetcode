"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def __init__(self) -> None:
        self.output = []

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root:
            self.output.append(root.val)
            for child in root.children:
                self.preorder(child)
        return self.output
