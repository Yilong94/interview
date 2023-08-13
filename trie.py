# At the end of a word, there should be a node with such an entry: {"*": None}
class TrieNode:
    def __init__(self):
        self.value = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for i in range(len(word)):
            char = word[i]

            if char not in current.value:
                current.value[char] = TrieNode()

            current = current.value[char]

        current.value["*"] = None

    def autocomplete(self, word):
        current = self.root

        for i in range(len(word)):
            char = word[i]
            if char not in current.value:
                return []

            current = current.value[char]

        result = []
        self.autocompleteRecur(current, word, result)
        return result

    def autocompleteRecur(self, current, state, result):
        for key, value in current.value.items():
            if key == "*":
                result.append(state)
            else:
                self.autocompleteRecur(value, state + key, result)
