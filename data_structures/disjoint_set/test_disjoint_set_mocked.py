import unittest
from unittest.mock import Mock, patch, MagicMock

# Assuming disjoint_set.py is in the same directory
# We import the functions and the class to be tested
from disjoint_set import Node, make_set, union_set, find_set


class TestDisjointSetMocked(unittest.TestCase):

    def test_node_initialization_mock_check(self):
        """Test the Node class setup using a Mock for comparison."""
        # This demonstrates creating a Mock to mirror the expected state
        mock_node = Mock(spec=Node)
        mock_node.data = 10
        
        n = Node(10)
        self.assertEqual(n.data, mock_node.data)
        # Note: We can't check rank/parent equivalence directly here 
        # as they are uninitialized but their existence is verified later.

    def test_make_set_mock_verification(self):
        """Test make_set and verify state using Mock attributes."""
        # Use MagicMock for a Node that can track attribute assignment
        n = MagicMock(spec=Node, data=5)
        
        # Call the function with the MagicMock
        make_set(n)
        
        # Verify the rank was set correctly
        self.assertEqual(n.rank, 0)
        
        # Verify the parent was set to itself (the mock object)
        self.assertIs(n.parent, n)

    @patch('disjoint_set.find_set')
    def test_union_set_equal_ranks_with_patch(self, mock_find_set):
        """Test union_set when ranks are equal, patching find_set behavior."""
        
        # 1. Setup Mock Nodes
        root_a = MagicMock(spec=Node, data=1, rank=1)
        root_b = MagicMock(spec=Node, data=2, rank=1)
        
        # 2. Patch the return values of find_set()
        # The first two calls to find_set (inside union_set) will return these roots
        mock_find_set.side_effect = [root_a, root_b]

        # 3. Execute union_set
        # It should call find_set(a) -> root_a and find_set(b) -> root_b
        union_set(Mock(), Mock()) # Pass dummy nodes, as find_set is mocked

        # 4. Assertions (Equal ranks: root_b should be parent of root_a, root_b.rank increases)
        
        # Check that root_b's rank was incremented
        self.assertEqual(root_b.rank, 2)
        
        # Check that root_a's parent was set to root_b
        self.assertIs(root_a.parent, root_b)
        
        # Check that root_b's parent and rank were not modified (it is the new root)
        # (Mock tracks calls, but we set the final state manually above for simplicity)
        
    @patch('disjoint_set.find_set')
    def test_union_set_different_ranks_with_patch(self, mock_find_set):
        """Test union_set when ranks are different (rank_a > rank_b)."""
        
        # 1. Setup Mock Nodes
        root_a = MagicMock(spec=Node, data=1, rank=2) # Higher rank
        root_b = MagicMock(spec=Node, data=2, rank=1)
        
        # 2. Patch the return values
        mock_find_set.side_effect = [root_a, root_b]

        # 3. Execute union_set
        union_set(Mock(), Mock()) 

        # 4. Assertions (root_a is the parent, ranks do not change)
        
        # Check that root_b's parent was set to root_a
        self.assertIs(root_b.parent, root_a)
        
        # Check that ranks were not changed
        self.assertEqual(root_a.rank, 2) # Still 2
        self.assertEqual(root_b.rank, 1) # Still 1

    def test_find_set_mock_recursive_call(self):
        """Test find_set path compression by mocking the parent."""
        
        # Create three Mock objects to form a chain: child -> intermediate -> root
        root = Mock(spec=Node, data=3)
        intermediate = Mock(spec=Node, data=2, parent=root)
        child = Mock(spec=Node, data=1, parent=intermediate)
        
        # The base case for the recursion (root.parent is root)
        root.parent = root
        
        # Set up the parent chain for path compression
        intermediate.parent = root
        child.parent = intermediate
        
        final_root = find_set(child)
        
        self.assertIs(final_root, root, "Should return the root node.")
        
        # Path compression check
        self.assertIs(child.parent, root, "Child's parent should be compressed to root.")
        self.assertIs(intermediate.parent, root, "Intermediate's parent should be compressed to root.")