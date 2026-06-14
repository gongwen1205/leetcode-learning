# -*- coding: utf-8 -*-

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # 94. 二叉树的中序遍历
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)
        return result

    # 94. 二叉树的中序遍历（迭代）
    def inorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        result, stack, curr = [], [], root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result

    # 226. 翻转二叉树
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    # 104. 二叉树的最大深度
    # 最大深度: 二叉树的根节点到最远叶子节点的最长路径上的节点数
    # maxDepth定义在类中是实例方法,必须通过self.调用
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    # 226. 翻转二叉树
    # 递归翻转左右子树顺序可以互换
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    
    # 101. 对称二叉树
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isSymmetricHelper(root.left, root.right)
    
    def isSymmetricHelper(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and self.isSymmetricHelper(left.left, right.right) and self.isSymmetricHelper(left.right, right.left)

    # 543. 二叉树的直径
    # 二叉树直径: 二叉树的左右子树最长路径上的节点数
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.diameterOfBinaryTreeHelper(root)
        return self.max_diameter
    
    def diameterOfBinaryTreeHelper(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height = self.diameterOfBinaryTreeHelper(root.left)
        right_height = self.diameterOfBinaryTreeHelper(root.right)
        self.max_diameter = max(self.max_diameter, left_height + right_height)
        return 1 + max(left_height, right_height)
    
    # 102. 二叉树的层序遍历
    # 层序遍历: 二叉树的每一层从左到右遍历
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def levelOrderHelper(node, level):
            if not node:
                return
            if len(result) == level:
                result.append([])
            result[level].append(node.val)
            levelOrderHelper(node.left, level + 1)
            levelOrderHelper(node.right, level + 1)
        levelOrderHelper(root, 0)
        return result   

    # 108. 将有序数组转换为二叉搜索树
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    # 98. 验证二叉搜索树
    # 二叉搜索树: 左子树所有节点值小于根节点值,右子树所有节点值大于根节点值
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidBSTHelper(root, float('-inf'), float('inf'))
    
    def isValidBSTHelper(self, root: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        if not root:
            return True
        if root.val <= min_val or root.val >= max_val:
            return False
        return self.isValidBSTHelper(root.left, min_val, root.val) and self.isValidBSTHelper(root.right, root.val, max_val)
    