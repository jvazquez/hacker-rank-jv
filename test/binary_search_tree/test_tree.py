# -*- coding: utf-8 -*-
"""
Author: Jorge Omar Vazquez <jorgeomar.vazquez@gmail.com>
"""
import logging

import unittest

from collections import deque

from binary_search_tree import tree


logger = logging.getLogger(__name__)


class NodeCompareIsLowerTestCase(unittest.TestCase):
    def test_node_compare_detects_lower_value(self):
        node = tree.Node(100)
        self.assertFalse(node.is_lower_than(20))

    def test_node_compare_detects_greater_value(self):
        node = tree.Node(100)
        self.assertTrue(node.is_lower_than(101))


class NodeCompareIsGreaterThanTestCase(unittest.TestCase):
    def test_node_compare_detects_greater_value(self):
        node = tree.Node(100)
        self.assertTrue(node.is_greater_than(20))

    def test_node_compare_detects_lower_value(self):
        node = tree.Node(100)
        self.assertFalse(node.is_greater_than(200))


class NodeInsertTestCase(unittest.TestCase):
    def test_node_insert(self):
        bst = tree.Node(100)
        bst.insert(5)
        bst.insert(101)
        self.assertEqual(bst.left.get_value(), 5)
        self.assertIsNotNone(bst.left)
        self.assertEqual(bst.right.get_value(), 101)
        self.assertIsNotNone(bst.right)

    def test_node_insert_duplicate(self):
        bst = tree.Node(10)
        bst.insert(10)
        self.assertIsNone(bst.left)
        self.assertIsNotNone(bst.right)
        self.assertEqual(bst.right.get_value(), 10)


class NodeDisplayTestCase(unittest.TestCase):
    def test_stack_inorder_will_not_trigger_exception(self):
        bst = tree.Node(10)
        bst.insert(5)
        bst.insert(10)
        bst.insert(4)
        bst.insert(11)
        bst.insert(11)
        witness = []
        try:
           bst.stack_inorder(witness)
        except AttributeError as e:
            self.fail("Should not have been an exception. Fail with:{}"
                      .format(e))
        expected = [4, 5, 10, 10, 11, 11]
        self.assertEqual(expected, witness)

    def test_stack_in_preorder_will_not_trigger_exception(self):
        bst = tree.Node(10)
        deque(map(lambda number: bst.insert(number), [11, 8, 3, 9]))
        try:
           collector = []
           bst.stack_in_preorder(collector)
        except AttributeError as e:
            self.fail("Should not have been an exception. Fail with:{}"
                      .format(e))
        self.assertEqual(bst.get_value(), 10)
        self.assertEqual(bst.left.get_value(), 8)
        self.assertEqual(bst.left.left.get_value(), 3)
        self.assertEqual(bst.left.right.get_value(), 9)
        self.assertEqual(bst.right.get_value(), 11)
        expected = [10, 8, 3, 9, 11]
        self.assertEqual(expected, collector)

    def test_stack_in_postorder_will_not_trigger_exception(self):
        bst = tree.Node(10)
        deque(map(lambda number: bst.insert(number), [11, 8, 3, 9]))
        try:
           collector = []
           bst.stack_in_postorder(collector)
        except AttributeError as e:
            self.fail("Should not have been an exception. Fail with:{}"
                      .format(e))
        expected = [3, 9, 8, 11, 10]
        self.assertEqual(expected, collector)


class NodeFindHeightTestCase(unittest.TestCase):
    def test_find_height_with_no_nodes(self):
        bst = tree.Node(10)
        height = bst.height()
        self.assertEqual(0, height)

    def test_find_height_returns_value(self):
        bst = tree.Node(10)
        deque(map(lambda number: bst.insert(number), [11, 8, 3, 9, 2]))
        height = bst.height()
        expected_height = 3
        self.assertEqual(height, expected_height)


class TestNodeIsBalanced(unittest.TestCase):
    def test_is_balanced(self): 
        bst = tree.Node(20)
        deque(map(lambda number: bst.insert(number), [22, 21, 25, 8, 3, 9]))
        self.assertTrue(bst.is_balanced())

    def test_is_balanced(self): 
        bst = tree.Node(20)
        deque(map(lambda number: bst.insert(number), [22, 21, 25, 8]))
        self.assertFalse(bst.is_balanced())


class TestNodeIsBst(unittest.TestCase):
    def test_is_bst_will_detect_single_node(self):
        bst = tree.Node(1)
        self.assertTrue(tree.is_bst(bst))

    def test_is_bst_will_detect_wrong_bst(self):
        bst = tree.Node(10)
        bst.right = tree.Node(1)
        bst.left = tree.Node(100)
        self.assertFalse(tree.is_bst(bst))

    def test_is_bst_will_detect_good_bst(self):
        bst = tree.Node(10)
        bst.right = tree.Node(11)
        bst.left = tree.Node(9)
        self.assertFalse(tree.is_bst(bst))

    def test_hacker_rank_input(self):
        bst = tree.Node(1)
        hacker_rank_list = [2, 2, 4, 5, 6, 7]
        deque(map(lambda number: bst.insert(number), hacker_rank_list))
        collector = []
        bst.stack_inorder(collector)
        self.assertEqual(collector, [1] + hacker_rank_list)
        self.assertFalse(tree.is_bst(bst))
        collector = []
        bst.stack_inorder(collector)
        # This solved this test case, yet the is_bst didn't pass the test.
        is_sorted = all(collector[i] < collector[i+1] for i in range(len(collector) - 1))
        self.assertFalse(is_sorted)

