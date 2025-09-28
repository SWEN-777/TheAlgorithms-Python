"""
Implements a disjoint set using Lists and some added heuristics for efficiency
Union by Rank Heuristic and Path Compression
"""


class DisjointSet:
    def __init__(self, set_counts: list) -> None:
        """
        Initialize with a list of the number of items in each set
        and with rank = 1 for each set

        >>> A = DisjointSet([1, 1, 1])
        >>> A.set_counts
        [1, 1, 1]
        >>> A.ranks
        [1, 1, 1]
        >>> A.parents
        [0, 1, 2]
        >>> A.max_set
        1
        """
        self.set_counts = set_counts
        self.max_set = max(set_counts)
        num_sets = len(set_counts)
        self.ranks = [1] * num_sets
        self.parents = list(range(num_sets))

    def merge(self, src: int, dst: int) -> bool:
        """
        Merge two sets together using Union by rank heuristic.
        Return True if merged, False if already in the same set.

        Basic usage:
        >>> A = DisjointSet([1, 1, 1])
        >>> A.merge(1, 2)
        True
        >>> A.merge(0, 2)
        True
        >>> A.merge(0, 1)
        False

        Edge case: merging a set with itself
        >>> B = DisjointSet([1, 2])
        >>> B.merge(0, 0)
        False

        Edge case: redundant merges should not inflate rank
        >>> C = DisjointSet([1, 1])
        >>> C.merge(0, 1)
        True
        >>> rank_before = C.ranks[C.get_parent(0)]
        >>> C.merge(0, 1)
        False
        >>> C.ranks[C.get_parent(0)] == rank_before
        True
        """
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        if self.ranks[dst_parent] >= self.ranks[src_parent]:
            self.set_counts[dst_parent] += self.set_counts[src_parent]
            self.set_counts[src_parent] = 0
            self.parents[src_parent] = dst_parent
            if self.ranks[dst_parent] == self.ranks[src_parent]:
                self.ranks[dst_parent] += 1
            joined_set_size = self.set_counts[dst_parent]
        else:
            self.set_counts[src_parent] += self.set_counts[dst_parent]
            self.set_counts[dst_parent] = 0
            self.parents[dst_parent] = src_parent
            joined_set_size = self.set_counts[src_parent]

        self.max_set = max(self.max_set, joined_set_size)
        return True

    def get_parent(self, disj_set: int) -> int:
        """
        Find the Parent of a given set (with path compression).

        >>> A = DisjointSet([1, 1, 1])
        >>> A.merge(1, 2)
        True
        >>> A.get_parent(0)
        0
        >>> A.get_parent(1) in (1, 2)  # 1's parent is compressed to 2
        True

        Edge case: a completely isolated set points to itself
        >>> B = DisjointSet([5, 10])
        >>> B.get_parent(0)
        0
        >>> B.get_parent(1)
        1
        """
        if self.parents[disj_set] == disj_set:
            return disj_set
        self.parents[disj_set] = self.get_parent(self.parents[disj_set])
        return self.parents[disj_set]
