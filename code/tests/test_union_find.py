import unittest
from union_find import initialize, find, union

class TestUnionFind(unittest.TestCase):
    def test_union_find(self):
        parent, rank = initialize(5)
        union(parent, rank, 0, 1)
        union(parent, rank, 1, 2)
        self.assertEqual(find(parent, 0), find(parent, 2))
        self.assertNotEqual(find(parent, 3), find(parent, 0))

if __name__ == "__main__":
    unittest.main()
