import unittest

from search_algorithms import (
    Trie,
    breadth_first_search,
    binary_search,
    depth_first_search,
    exponential_search,
    fibonacci_search,
    interpolation_search,
    jump_search,
    linear_search,
    sentinel_search,
    ternary_search,
)


class SequentialSearchTests(unittest.TestCase):
    def test_linear_search_returns_first_match(self) -> None:
        self.assertEqual(linear_search([5, 2, 5], 5), 0)
        self.assertEqual(linear_search([], 5), -1)

    def test_sentinel_search(self) -> None:
        self.assertEqual(sentinel_search([1, 4, 9], 4), 1)
        self.assertEqual(sentinel_search([1, 4, 9], 7), -1)
        self.assertEqual(sentinel_search([], 7), -1)


class OrderedSearchTests(unittest.TestCase):
    def test_every_ordered_search_handles_present_and_missing_values(self) -> None:
        algorithms = (
            binary_search,
            exponential_search,
            fibonacci_search,
            interpolation_search,
            jump_search,
            ternary_search,
        )
        for algorithm in algorithms:
            with self.subTest(algorithm=algorithm.__name__):
                for values in ([], [3], [2, 5, 9, 14, 21, 28, 35, 44]):
                    for target in range(0, 47):
                        result = algorithm(values, target)
                        if target in values:
                            self.assertEqual(values[result], target)
                        else:
                            self.assertEqual(result, -1)

    def test_duplicate_and_constant_values(self) -> None:
        self.assertIn(binary_search([4, 4, 4], 4), range(3))
        self.assertEqual(interpolation_search([4, 4, 4], 4), 0)
        self.assertEqual(interpolation_search([4, 4, 4], 5), -1)


class GraphSearchTests(unittest.TestCase):
    def setUp(self) -> None:
        self.graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D", "E"],
            "D": [],
            "E": [],
        }

    def test_breadth_first_search_returns_shortest_path(self) -> None:
        self.assertEqual(breadth_first_search(self.graph, "A", "E"), ["A", "C", "E"])
        self.assertEqual(breadth_first_search(self.graph, "A", "A"), ["A"])
        self.assertIsNone(breadth_first_search(self.graph, "A", "missing"))

    def test_depth_first_search_returns_a_valid_path(self) -> None:
        path = depth_first_search(self.graph, "A", "D")
        self.assertIsNotNone(path)
        self.assertEqual(path[0], "A")
        self.assertEqual(path[-1], "D")
        self.assertTrue(all(right in self.graph[left] for left, right in zip(path, path[1:])))


class TrieTests(unittest.TestCase):
    def test_insert_search_and_prefix(self) -> None:
        trie = Trie()
        trie.insert("search")
        trie.insert("sea")
        self.assertTrue(trie.search("search"))
        self.assertTrue(trie.search("sea"))
        self.assertFalse(trie.search("se"))
        self.assertTrue(trie.starts_with("sear"))
        self.assertTrue(trie.starts_with(""))
        self.assertFalse(trie.starts_with("xyz"))


if __name__ == "__main__":
    unittest.main()
