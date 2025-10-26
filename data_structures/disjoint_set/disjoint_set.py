"""
Disjoint set.
Reference: https://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""


class Node:
    def __init__(self, data: int) -> None:
        """
        Create a new Node.

        >>> n = Node(5)
        >>> isinstance(n, Node)
        True
        >>> n.data
        5
        """
        self.data = data
        self.rank: int = None
        self.parent: "Node" = None


def make_set(x: Node) -> None:
    """
    Make x its own parent (a new set).

    >>> n = Node(1)
    >>> make_set(n)
    >>> n.rank
    0
    >>> n.parent is n
    True
    """
    x.rank = 0
    x.parent = x


def union_set(x: Node, y: Node) -> None:
    """
    Union of two sets.
    The set with the bigger rank should become parent,
    keeping the disjoint set tree flatter.

    >>> a, b = Node(1), Node(2)
    >>> make_set(a); make_set(b)
    >>> union_set(a, b)
    >>> find_set(a) == find_set(b)
    True

    Union with itself does nothing:
    >>> union_set(a, a)
    >>> find_set(a) == find_set(b)
    True

    Redundant unions do not change ranks:
    >>> rank_before = find_set(a).rank
    >>> union_set(a, b)
    >>> find_set(a).rank == rank_before
    True
    """
    x, y = find_set(x), find_set(y)
    if x == y:
        return

    elif x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def find_set(x: Node) -> Node:
    """
    Return the representative parent of x (with path compression).

    >>> a, b, c = Node(0), Node(1), Node(2)
    >>> make_set(a); make_set(b); make_set(c)
    >>> union_set(a, b)
    >>> union_set(b, c)
    >>> find_set(a) == find_set(c)
    True

    Isolated node points to itself:
    >>> n = Node(99)
    >>> make_set(n)
    >>> find_set(n) == n
    True
    """
    if x != x.parent:
        x.parent = find_set(x.parent)
    return x.parent


def find_python_set(node: Node) -> set:
    """
    Return a Python set that contains node.data.

    >>> a = Node(0)
    >>> make_set(a)
    >>> find_python_set(a)
    {0, 1, 2}

    Raises ValueError if not found:
    >>> n = Node(99)
    >>> make_set(n)
    >>> find_python_set(n)
    Traceback (most recent call last):
        ...
    ValueError: 99 is not in ({0, 1, 2}, {3, 4, 5})
    """
    sets = ({0, 1, 2}, {3, 4, 5})
    for s in sets:
        if node.data in s:
            return s
    msg = f"{node.data} is not in {sets}"
    raise ValueError(msg)