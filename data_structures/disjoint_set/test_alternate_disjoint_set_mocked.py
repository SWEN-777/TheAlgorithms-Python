import unittest
from unittest.mock import Mock, patch, MagicMock

# Assuming alternate_disjoint_set.py is in the same directory
from alternate_disjoint_set import DisjointSet


class TestAlternateDisjointSetMocked(unittest.TestCase):
    
    def setUp(self):
        """Initialize a standard DisjointSet instance for testing."""
        self.ds = DisjointSet([1, 1, 1, 1]) # 4 sets, all size 1, rank 1

    @patch.object(DisjointSet, 'get_parent')
    def test_merge_no_op_with_mocked_parent(self, mock_get_parent):
        """Test merge when sets are already joined, using a mocked get_parent."""
        
        # Mock get_parent to always return the same root index (e.g., 2)
        mock_get_parent.return_value = 2

        # Try to merge set 0 and set 1
        result = self.ds.merge(0, 1)

        # Assert merge failed (already in the same set)
        self.assertFalse(result)
        
        # Assert get_parent was called twice (for src and dst)
        mock_get_parent.assert_any_call(0)
        mock_get_parent.assert_any_call(1)
        self.assertEqual(mock_get_parent.call_count, 2)
        
        # Assert internal state (parents/ranks) was NOT modified
        self.assertEqual(self.ds.parents, [0, 1, 2, 3])

    @patch.object(DisjointSet, 'get_parent')
    def test_merge_rank_dst_wins_with_mocked_parent(self, mock_get_parent):
        """Test merge where dst has higher rank, using a mocked get_parent."""
        
        SRC, DST = 0, 1
        
        # 1. Manually set up ranks and counts (to mock pre-existing state)
        self.ds.ranks = [1, 2, 1, 1]  # DST (index 1) has higher rank
        self.ds.set_counts = [5, 10, 1, 1] 
        self.ds.max_set = 10
        
        # 2. Mock get_parent to return the root indices (which are SRC and DST)
        # Sequence: get_parent(src) -> SRC, get_parent(dst) -> DST
        mock_get_parent.side_effect = [SRC, DST] 

        # 3. Execute merge
        self.assertTrue(self.ds.merge(SRC, DST))

        # 4. Assertions (SRC's root should point to DST's root)
        
        # DST (index 1) is the parent of SRC (index 0)
        self.assertEqual(self.ds.parents[SRC], DST)
        
        # DST's rank should NOT increase (since DST.rank > SRC.rank)
        self.assertEqual(self.ds.ranks[DST], 2)
        
        # Set counts updated: DST_count += SRC_count, SRC_count = 0
        self.assertEqual(self.ds.set_counts[DST], 15)
        self.assertEqual(self.ds.set_counts[SRC], 0)
        self.assertEqual(self.ds.max_set, 15)
