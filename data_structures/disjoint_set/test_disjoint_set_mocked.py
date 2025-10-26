import unittest
from unittest.mock import Mock, patch, MagicMock
from data_structures.disjoint_set.disjoint_set import Node, make_set, union_set, find_set


class TestDisjointSetMocked(unittest.TestCase):

    def test_node_initialization_mock_check(self):
        mock_node = Mock(spec=Node)
        mock_node.data = 10
        n = Node(10)
        self.assertEqual(n.data, mock_node.data)

    def test_node_initialization_defaults(self):
        """Covers mutation from None → True and None → False in Node.__init__"""
        n = Node(42)
        self.assertEqual(n.data, 42)
        self.assertTrue(hasattr(n, "parent"))
        self.assertTrue(hasattr(n, "rank"))
        self.assertIsNone(n.parent)
        self.assertIsNone(n.rank)

    def test_node_parent_is_none_before_make_set(self):
        """Kills mutation from None → True in Node.__init__"""
        n = Node(42)
        self.assertIsNone(n.parent)
        self.assertIsNot(n.parent, True)

    def test_make_set_mock_verification(self):
        n = MagicMock(spec=Node, data=5)
        make_set(n)
        self.assertEqual(n.rank, 0)
        self.assertIs(n.parent, n)

    def test_make_set_parent_is_not_true(self):
        """Kills mutation from None → True in make_set"""
        n = Node(99)
        make_set(n)
        self.assertIs(n.parent, n)
        self.assertIsNot(n.parent, True)

    def test_make_set_parent_is_not_false(self):
        """Kills mutation from None → False in make_set"""
        n = Node(99)
        make_set(n)
        self.assertIs(n.parent, n)
        self.assertIsNot(n.parent, False)

    def test_make_set_rank_is_not_false(self):
        """Additional check for rank mutation"""
        n = Node(99)
        make_set(n)
        self.assertEqual(n.rank, 0)
        self.assertIsNot(n.rank, False)

    @patch('data_structures.disjoint_set.disjoint_set.find_set')
    def test_union_set_equal_ranks_with_patch(self, mock_find_set):
        root_a = MagicMock(spec=Node, data=1, rank=1)
        root_b = MagicMock(spec=Node, data=2, rank=1)
        mock_find_set.side_effect = [root_a, root_b]
        union_set(Mock(), Mock())
        self.assertEqual(root_b.rank, 2)
        self.assertIs(root_a.parent, root_b)

    @patch('data_structures.disjoint_set.disjoint_set.find_set')
    def test_union_set_different_ranks_with_patch(self, mock_find_set):
        root_a = MagicMock(spec=Node, data=1, rank=2)
        root_b = MagicMock(spec=Node, data=2, rank=1)
        mock_find_set.side_effect = [root_a, root_b]
        union_set(Mock(), Mock())
        self.assertIs(root_b.parent, root_a)
        self.assertEqual(root_a.rank, 2)
        self.assertEqual(root_b.rank, 1)

    def test_find_set_mock_recursive_call(self):
        root = Mock(spec=Node, data=3)
        intermediate = Mock(spec=Node, data=2, parent=root)
        child = Mock(spec=Node, data=1, parent=intermediate)
        root.parent = root
        intermediate.parent = root
        child.parent = intermediate
        final_root = find_set(child)
        self.assertIs(final_root, root)
        self.assertIs(child.parent, root)
        self.assertIs(intermediate.parent, root)

    def test_find_set_parent_identity_not_true(self):
        """Kills mutation from None → True in find_set"""
        root = Node(1)
        root.parent = root
        child = Node(2)
        child.parent = root
        result = find_set(child)
        self.assertIs(result, root)
        self.assertIs(child.parent, root)
        self.assertIsNot(child.parent, True)
