# -*- coding: utf-8 -*-
"""
Author: Jorge Omar Vazquez <jorgeomar.vazquez@gmail.com>
"""
import logging

from binary_search_tree.constants import MAXIMUM, MINIMUM

logger = logging.getLogger(__name__)


class Node:
    def __init__(self, value):
        """ Representation of a binary tree """

        self.data = value
        self.left = None
        self.right = None

    def is_lower_than(self, value):
        """ Determine if the provided information is lower than
        the node value.
        Returns:
            boolean
        """

        return self.data < value

    def is_greater_than(self, value):
        """ Determine if the provided information is greater than
        the node value.
        Returns:
            boolean
        """

        return self.data > value

    def height(self):
        """Obtains the height of a tree
        Returns
            int
        """
        height_left = self.left.height() if self.left else -1
        height_right = self.right.height() if self.right else -1
        return max(height_left, height_right) + 1

    def is_balanced(self):
        height_left = self.left.height() if self.left else -1
        height_right = self.right.height() if self.right else -1

        balanced_left = self.left.is_balanced() if self.left else False
        balanced_right = self.right.is_balanced() if self.right else False

        if(abs(height_left - height_right) <=1
           and balanced_left and balanced_right):
            return True
        return False

    def get_value(self):
        """ Return the value of the current node """

        return self.data

    def insert(self, value):
        if self.is_greater_than(value):
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def display_in_order(self):
        if self.left is not None:
            self.left.display_in_order()

        print("{}".format(self.data))

        if self.right is not None:
            self.right.display_in_order()

    def stack_inorder(self, stack):
        """Stacks the elements of the tree
        in order

        Parameters:
            stack `list`: A list that will store in order the values from the
            tree. Keep in mind the size of the tree before using this method.
        """

        if self.left is not None:
            self.left.stack_inorder(stack)

        stack.append(self.get_value())

        if self.right is not None:
            self.right.stack_inorder(stack)

    def stack_in_preorder(self, stack):
        stack.append(self.get_value())

        if self.left:
            self.left.stack_in_preorder(stack)

        if self.right:
            self.right.stack_in_preorder(stack)

    def stack_in_postorder(self, stack):
        if self.left:
            self.left.stack_in_postorder(stack)

        if self.right:
            self.right.stack_in_postorder(stack)

        stack.append(self.get_value())


def is_bst(node):
    return _is_bst_scan(node, MINIMUM, MAXIMUM) 

def _is_bst_scan(node, minimum, maximum):
    if node is None:
        return True

    return (node.data > minimum and node.data < maximum and
            _is_bst_scan(node.left, minimum, node.data - 1) and
            _is_bst_scan(node.right, node.data + 1, maximum))

