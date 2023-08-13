import unittest
from trie import *


class TestTrie(unittest.TestCase):
    def test_insert(self):
        trie = Trie()
        trie.insert("ace")
        trie.insert("act")
        trie.insert("bad")
        trie.insert("bake")
        trie.insert("bat")
        trie.insert("batter")
        trie.insert("cab")
        trie.insert("cat")
        trie.insert("catnap")
        trie.insert("catnip")

        # First-level nodes
        self.assertEqual(
            trie.root.value,
            {
                "a": trie.root.value["a"],
                "b": trie.root.value["b"],
                "c": trie.root.value["c"],
            },
        )

        # Second-level nodes
        self.assertEqual(
            trie.root.value["a"].value,
            {
                "c": trie.root.value["a"].value["c"],
            },
        )
        self.assertEqual(
            trie.root.value["b"].value,
            {
                "a": trie.root.value["b"].value["a"],
            },
        )
        self.assertEqual(
            trie.root.value["c"].value,
            {
                "a": trie.root.value["c"].value["a"],
            },
        )

        # Third-level nodes
        self.assertEqual(
            trie.root.value["a"].value["c"].value,
            {
                "e": trie.root.value["a"].value["c"].value["e"],
                "t": trie.root.value["a"].value["c"].value["t"],
            },
        )
        self.assertEqual(
            trie.root.value["b"].value["a"].value,
            {
                "d": trie.root.value["b"].value["a"].value["d"],
                "k": trie.root.value["b"].value["a"].value["k"],
                "t": trie.root.value["b"].value["a"].value["t"],
            },
        )
        self.assertEqual(
            trie.root.value["c"].value["a"].value,
            {
                "b": trie.root.value["c"].value["a"].value["b"],
                "t": trie.root.value["c"].value["a"].value["t"],
            },
        )

        # Fourth-level nodes
        self.assertEqual(
            trie.root.value["a"].value["c"].value["e"].value,
            {
                "*": None,
            },
        )
        self.assertEqual(
            trie.root.value["a"].value["c"].value["t"].value,
            {
                "*": None,
            },
        )
        self.assertEqual(
            trie.root.value["b"].value["a"].value["d"].value,
            {
                "*": None,
            },
        )
        self.assertEqual(
            trie.root.value["b"].value["a"].value["k"].value,
            {
                "e": trie.root.value["b"].value["a"].value["k"].value["e"],
            },
        )
        self.assertEqual(
            trie.root.value["b"].value["a"].value["t"].value,
            {"*": None, "t": trie.root.value["b"].value["a"].value["t"].value["t"]},
        )
        self.assertEqual(
            trie.root.value["c"].value["a"].value["b"].value,
            {
                "*": None,
            },
        )
        self.assertEqual(
            trie.root.value["c"].value["a"].value["t"].value,
            {"*": None, "n": trie.root.value["c"].value["a"].value["t"].value["n"]},
        )

        # Fifth-level nodes (some...)
        self.assertEqual(
            trie.root.value["b"].value["a"].value["k"].value["e"].value,
            {
                "*": None,
            },
        )
        self.assertEqual(
            trie.root.value["b"].value["a"].value["t"].value["t"].value,
            {"e": trie.root.value["b"].value["a"].value["t"].value["t"].value["e"]},
        )

        # Sixth-level nodes (some...)
        self.assertEqual(
            trie.root.value["b"].value["a"].value["t"].value["t"].value["e"].value,
            {
                "r": trie.root.value["b"]
                .value["a"]
                .value["t"]
                .value["t"]
                .value["e"]
                .value["r"]
            },
        )

        # Seventh-level nodes (some...)
        self.assertEqual(
            trie.root.value["b"]
            .value["a"]
            .value["t"]
            .value["t"]
            .value["e"]
            .value["r"]
            .value,
            {"*": None},
        )

    def test_autocomplete(self):
        trie = Trie()
        trie.insert("ace")
        trie.insert("act")
        trie.insert("bad")
        trie.insert("bake")
        trie.insert("bat")
        trie.insert("batter")
        trie.insert("cab")
        trie.insert("cat")
        trie.insert("catnap")
        trie.insert("catnip")

        tests = [
            {"word": "cat", "expected": ["cat", "catnap", "catnip"]},
            {"word": "a", "expected": ["ace", "act"]},
            {"word": "bake", "expected": ["bake"]},
            {"word": "dog", "expected": []},
        ]
        for tt in tests:
            self.assertEqual(trie.autocomplete(tt["word"]), tt["expected"])


if __name__ == "__main__":
    unittest.main()
